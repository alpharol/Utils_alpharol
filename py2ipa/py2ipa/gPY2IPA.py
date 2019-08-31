#!/usr/bin/env python
# This file has following encoding: utf-8
######################## 模块文档 ########################
U"""汉语拼音-国际音标转换工具 2.1版（2007年9月16日）

作者：徐清白(http://xuqingbai.googlepages.com)，首发于2007年8月6日
授权：自由软件（GNU 通用公共许可证）

依赖：Python 解释器 2.5 或更新版本
      wxPython 接口库 2.8.4版（建议）
      py2ipa.py 脚本文件

文稿格式：<单字拼音>[[ |']<更多单字拼音>...]
其中：<单字拼音> = <汉语拼音字母串>[<声调标号>]
      <声调标号> 取值1-5（对应四声和轻声）

标音风格：适度严格的IPA音素音标＋部分汉语言学界专用符号

特别声明：转换结果仅供学习参考！

详细的用户文档请参看“DOC_USERSGUIDE.html”文件"""
######################## 模块导入 ########################
import wx      # wxPython接口库
import py2ipa  # 汉语拼音-国际音标转换工具
######################## 全局变量 ########################
document = __doc__
# 窗口标题
mainFrameTitle = document[:document.index(U"版")+1]  # 截取"XXXXXX ?.?版"
prefFrameTitle = U"设置转换规则"
# 拼音文稿输入区初始内容
initPinyin = U"""Han4yu3 pin1yin1 yong4chu duo1
#Han4yu3 pin1yin1 yong4chu duo1
汉语拼音用处多"""
# wx.Point类型的标志
X, Y = 0, 1
# 收集名称包含“recipe”字样的对象，构造一揽子创建设置方案库（列表）
py2ipa.recipe = (U"（经典一揽子设置方案在此选择）",)
cookBook = map(eval, ["py2ipa."+id for id in [id for id in dir(py2ipa) if "recipe" in id]])
# 转换规则设置表和内部标志
prefList = (
  [0, "NUMBER_2_BY_AR4",                   U"数字“二”有大开口度韵腹"],
  [0, "AI_INC_NEAR_OPEN_FRONT",            U"ai/uai韵腹为舌面前次开元音"],
  [0, "AIR_ANR_INC_NEAR_OPEN_CENTRAL",     U"air/anr韵腹为舌面央次低元音"],
  [0, "CENTRAL_A_BY_SMALLCAPS_A",          U"“央a”采用小型大写[A]标明"],
  [0, "IE_YUE_INC_SMALLCAPS_E",            U"ie/yue采用小型大写[E]标明"],
  [0, "IE_YUE_INC_E",                      U"ie/yue采用[e]标明（覆盖上一条规则）"],
  [0, "IAN_YUAN_AS_AN",                    U"ian/yuan韵腹和an一样"],
  [0, "ONLY_YUAN_AS_AN",                   U"仅yuan韵腹和an一样（覆盖上一条规则）"],
  [0, "OU_INC_SCHWA",                      U"ou/iou采用舌面央中元音韵腹"],
  [0, "IONG_BY_IUNG",                      U"iong韵母采用i韵头u韵腹"],
  [0, "ONLY_ER_BY_RHOTIC_HOOK",            U"er音节卷舌动作采用卷舌小钩"],
  [0, "RHOTICITY_BY_RHOTIC_HOOK",          U"所有卷舌动作采用卷舌小钩（覆盖上一条规则）"],
  [0, "INITIAL_R_BY_VED_RETRO_FRIC",       U"声母r为卷舌浊擦音而非卷舌通音"],
  [0, "R_TURNED_WITH_HOOK",                U"严格采用卷舌通音符号"],
  [0, "TRANSITIONAL_SCHWA_IN_ING",         U"ing有舌面央中元音韵腹"],
  [0, "TRANSITIONAL_SCHWA_IN_UEN",         U"合口un有舌面央中元音韵腹"],
  [0, "NO_TRANSITIONAL_U",                 U"bo/po/mo/fo没有[u]韵头"],
  [0, "ASPIRATE_BY_TURNED_COMMA",          U"采用反逗号弱送气符号"],
  [0, "SYLLABLE_JUNCTURE_BY_PLUS",         U"音节间断采用开音渡+号而非.号"],
  [0, "HTML_SUP_TAG_FOR_TONE_VALUE",       U"调值采用HTML上标标签格式"],
  [0, "HIDE_ALL_TONE_VALUE",               U"隐藏所有声调转换（覆盖上一条规则）"],
### 以下选项仅存设想，目前尚未实现：
# [0, "RETROFLEX_INITIAL_STANDALONE",      U"卷舌声母可成音节而无需舌尖元音"],
# [0, "ZERO_INITIAL_HAS_CONSONANT",        U"零声母有辅音"],
)
CHOICE, NAME, CAPTION = 0, 1, 2  # 标志：选择段、内部名称段、外部名称段
# 设置表字典，用于根据一揽子设置方案反查选项
prefDict = dict()
for eachPref in prefList:
    prefDict[eachPref[NAME]] = eachPref[CAPTION]
# 一揽子设置方案下拉框初始选项
selectedRecipe = 0
######################## 界面定义 ########################
class mainFrame(wx.Frame):
    U"""主窗口"""
    def __init__(self, parent=None, id=-1, pos=wx.DefaultPosition,
         title=mainFrameTitle, size=(640, 460)):
        U"""主窗口初始化"""
        ### 全局设定
        wx.Frame.__init__(self, parent, id, title, pos, size)
        self.colTextCtrl = wx.Color(0, 0, 128, 255)  # 藏青色
        self.fonTextCtrl = wx.Font(12, wx.FONTFAMILY_ROMAN,
          wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, underline=False,
          face="Charis SIL", encoding=wx.FONTENCODING_DEFAULT)
        self.autoConvert = True  # 自动转换标志
        ### 构造控件
        panel = wx.Panel(self, -1)
        # 多行文本：拼音文稿输入
        wx.StaticText(panel, -1, U"请输入汉语拼音：", pos=(10, 10))  # 提示
        self.txtPinyinLines = wx.TextCtrl(panel, -1, initPinyin,
          pos=(10, 30), size=(615, 180), style=wx.TE_MULTILINE|wx.TE_RICH)
        self.txtPinyinLines.SetDefaultStyle(wx.TextAttr(colText=self.colTextCtrl,
          font=self.fonTextCtrl))
        self.txtPinyinLines.SetInsertionPoint(0)
        self.Bind(wx.EVT_TEXT, self.doAutoConvert, self.txtPinyinLines)
        # 按钮：设置转换规则
        self.butShowPrefFrame = wx.Button(panel, -1, U"设置转换规则(&R)...", pos=(10, 215))
        self.Bind(wx.EVT_BUTTON, self.showPrefFrame, self.butShowPrefFrame)
        self.butShowPrefFrame.SetDefault()  # 设为默认按钮
        # 按钮：立刻转换
        self.butConvert = wx.Button(panel, -1, U"立刻转换(&C)", pos=(135, 215))
        self.Bind(wx.EVT_BUTTON, self.doManualConvert, self.butConvert)
        # 复选：自动转换
        self.chkAutoConvert = wx.CheckBox(panel, -1, U"自动转换(&A)",
          pos=(self.butConvert.Position[X]+90, 220))
        self.chkAutoConvert.SetValue(True)
        self.Bind(wx.EVT_CHECKBOX, self.toggleAutoConvert, self.chkAutoConvert)
        # 按钮：复制结果
        self.butYankResult = wx.Button(panel, -1, U"复制结果(&Y)", pos=(315, 215))
        self.Bind(wx.EVT_BUTTON, self.copyIPA, self.butYankResult)
        # 按钮：选择字体
        self.butPickFont = wx.Button(panel, -1, U"选择字体(&F)...", pos=(400, 215))
        self.butPickFont.Bind(wx.EVT_BUTTON, self.pickFont)
        # 按钮：关于本品
        self.butAbout = wx.Button(panel, -1, U"关于(&B)...", pos=(495, 215), size=(67, 24))
        self.Bind(wx.EVT_BUTTON, self.aboutProgram, self.butAbout)
        # 按钮：退出
        self.butQuit = wx.Button(panel, -1, U"退出(&Q)", pos=(565, 215), size=(60, 24))
        self.Bind(wx.EVT_BUTTON, self.quitProgram, self.butQuit)
        # 多行文本：国际音标文稿输出
        self.txtIPALines = wx.TextCtrl(panel, -1, "", pos=(10, 245),
          size=(615, 180), style=wx.TE_MULTILINE|wx.TE_RICH|wx.TE_READONLY)
        ### 启动过程
        py2ipa.createCmdPairTuple()  # 第一次创建替换命令元组
        self.invokePinyin2IPA()      # 执行初始转换
    # 纯自由方法
    def keepTextAttr(self):
        U"""保持文字样式"""
        self.txtPinyinLines.SetStyle(0, len(self.txtPinyinLines.GetValue()),
          wx.TextAttr(colText=self.colTextCtrl, font = self.fonTextCtrl))
        self.txtIPALines.SetStyle(0, len(self.txtIPALines.GetValue()),
          wx.TextAttr(colText=self.colTextCtrl, font = self.fonTextCtrl))
    def invokePinyin2IPA(self):
        U"""调用转换函数"""
        pinyinLines = self.txtPinyinLines.GetValue().splitlines(True)
        self.txtIPALines.SetValue(py2ipa.convertPinyin2IPA(pinyinLines))
        self.keepTextAttr()  # 保持文字样式
    # 事件响应方法
    def showPrefFrame(self, event):
        U"""打开设置窗口self.frmPref（对准窗口和按钮）"""
        try:                    #尝试激活旧的设置窗口
            if self.frmPref:
                self.frmPref.butClose.SetFocus()
                return
        except AttributeError:  # 如果没有，则什么也不用做
            pass
        # 现在打开新的设置窗口
        self.frmPref = prefFrame(parent=self, pos=self.Position, size=(480,self.Size[Y]))
        self.frmPref.Show()
    def doManualConvert(self, event):
        U"""手动转换（按下命令按钮）"""
        self.invokePinyin2IPA()
    def doAutoConvert(self, event):
        U"""自动转换（根据self.autoConvert的设置）"""
        if self.autoConvert:
            self.invokePinyin2IPA()
        else:  # 保持文字样式
            self.keepTextAttr()
    def toggleAutoConvert(self, event):
        U"""切换自动转换选项"""
        self.autoConvert = not self.autoConvert
        if self.autoConvert:  # 改为自动转换后，立刻转换一次
            self.invokePinyin2IPA()
    def copyIPA(self, event):
        U"""将国际音标文稿复制到剪贴板"""
        text_data = wx.TextDataObject(self.txtIPALines.GetValue())
        if wx.TheClipboard.Open():
            wx.TheClipboard.SetData(text_data)
            wx.TheClipboard.Flush()
            wx.TheClipboard.Close()
    def pickFont(self, event):
        U"""由用户选择字体和颜色（删除线修饰无效）"""
        # 设置对话框的初始内容
        iniFont = wx.FontData()
        iniFont.SetAllowSymbols(True)       # 国际音标字体必需
        iniFont.SetColour(self.colTextCtrl)
        iniFont.SetInitialFont(self.fonTextCtrl)
        # 创建并弹出对话框
        dialog = wx.FontDialog(self, iniFont)
        if dialog.ShowModal() == wx.ID_OK:  # 确定：改变字体
            data = dialog.GetFontData()
            self.colTextCtrl = data.GetColour()
            self.fonTextCtrl = data.GetChosenFont()
            self.keepTextAttr()
        dialog.Destroy()
    def aboutProgram(self, event):
        U"""弹出关于本程序的消息对话框"""
        wx.MessageBox(document, U"关于“%s”"%mainFrameTitle)
    def quitProgram(self, event):
        U"""退出程序"""
        self.Close()
class prefFrame(wx.Frame):
    U"""设置窗口"""
    def __init__(self, parent, pos, size, id=-1, title=prefFrameTitle):
        U"""设置窗口初始化"""
        ### 全局设定
        wx.Frame.__init__(self, parent, id, title, pos, size,
          style=wx.FRAME_NO_TASKBAR|wx.DEFAULT_FRAME_STYLE)
        ### 构造控件
        panel = wx.Panel(self, -1)
        # 按钮：关闭设置窗口
        self.butClose = wx.Button(panel, -1, U"关闭设置窗口(&R)",
          pos=(self.Parent.butShowPrefFrame.Position[X],
          self.Parent.butShowPrefFrame.Position[Y]))
        self.Bind(wx.EVT_BUTTON, self.closePrefFrame, self.butClose)
        # 按钮：清空转换规则
        self.butClearPref = wx.Button(panel, -1, U"清空转换规则(&C)",
          pos=(self.butClose.Position[X], self.butClose.Position[Y] + 30))
        self.Bind(wx.EVT_BUTTON, self.clearPref, self.butClearPref)
        # 下拉列表：一揽子设置方案
        self.choCookBook = wx.Choice(panel, -1, (130, 10), (330, 1),
          choices=[item[CHOICE] for item in cookBook])
        self.resetRecipe(selectedRecipe)  # 初次定位
        self.Bind(wx.EVT_CHOICE, self.selectRecipe, self.choCookBook)
        # 复选列表：设置表
        self.chklbPref = wx.CheckListBox(panel, -1, (130, 40), (330, 380),
          choices=[item[CAPTION] for item in prefList], style=wx.LB_SINGLE)
        for prefNum in range(len(prefList)):    # 填入当前设置表的值
            self.chklbPref.Check(prefNum, prefList[prefNum][CHOICE])
        self.Bind(wx.EVT_CHECKLISTBOX, self.updatePref, self.chklbPref)
        self.Bind(wx.EVT_LISTBOX, self.clickPref, self.chklbPref)
    # 纯自由函数
    def resetRecipe(self, n=0):
        U"""复位一揽子设置方案下拉列表
        参数n供初次定位使用"""
        global selectedRecipe
        selectedRecipe = n  # 这两句主要用于将初始选项复位到0
        self.choCookBook.SetSelection(n)
    # 事件响应函数
    def closePrefFrame(self, event):
        U"""关闭设置窗口"""
        self.Close()
    def clearPref(self, event):
        U"""清空设置表"""
        for prefNum in range(len(prefList)):
            self.chklbPref.Check(prefNum, False)
        if event:                  # 当从self.selectRecipe()函数调用时
            self.resetRecipe()     # 不复位下拉框
            self.updatePref(None)  # 也无需在此时更新
    def updatePref(self, event):
        U"""更新设置表，重建替换命令元组"""
        if event:
            self.resetRecipe()
        global prefList
        newPref = list()
        for prefNum in range(len(prefList)):
            prefList[prefNum][CHOICE] = self.chklbPref.IsChecked(prefNum)
            if prefList[prefNum][CHOICE]:
                newPref.append(prefList[prefNum][NAME])
        py2ipa.createCmdPairTuple(newPref)
        if self.Parent.autoConvert:
            self.Parent.invokePinyin2IPA()
    def clickPref(self, event):
        U"""单击设置项，也等于切换设置项"""
        n = self.chklbPref.GetSelection()
        self.chklbPref.Check(n, not self.chklbPref.IsChecked(n))
        self.resetRecipe()
        self.updatePref(None)
    def selectRecipe(self, event):
        U"""选择一揽子设置方案"""
        global selectedRecipe      # 修改初始选项
        selectedRecipe = self.choCookBook.GetSelection()
        if selectedRecipe:         # 排除提示项
            self.clearPref(None)   # 先清空，但不复位下拉框，也不更新
            for eachCaption in [prefDict[name] for name in cookBook[selectedRecipe][1:]]:
                self.chklbPref.Check(self.chklbPref.FindString(eachCaption), True)
            self.updatePref(None)  # 这时才用更新
######################## 程序定义 ########################
class App(wx.App):
    U"""汉语拼音-国际音标转换工具 图形界面程序"""
    def OnInit(self):
        U"""构造主窗口self.frmMain并打开"""
        self.frmMain = mainFrame()
        self.frmMain.Show()
        self.SetTopWindow(self.frmMain)
        return True
######################## 主干函数 ########################
def main():
    U"""构造主程序app_gPY2IPA并运行"""
    wx.SetDefaultPyEncoding('utf8')
    app_gPY2IPA = App()
    app_gPY2IPA.MainLoop()
######################## 直接运行 ########################
if __name__ == '__main__':
    main()
######################## 脚本结束 ########################
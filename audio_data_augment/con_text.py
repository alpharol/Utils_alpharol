#读取文本文件
f = open("chanxian_15230_v4/chanxian_15230.pinyin","r")
con_1 = f.readlines()
f.close()

f = open("chepai_1758/chepai_1758.pinyin","r")
con_2 = f.readlines()
f.close()

f = open("output_text.txt","r")
con_3 = f.readlines()
f.close()

#文本数据拼接
con = con_1 + con_2 + con_3

#写入文件
for i in range(len(con)):
    con[i] = bytes(con[i],encoding = "utf-8")

f = open("metadata.txt","wb")
f.writelines(con)
f.close

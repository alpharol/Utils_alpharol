# CMU_dict

<br/>

##### 将英文的句子转化为 [CMU 发音词典](http://www.speech.cs.cmu.edu/cgi-bin/cmudict)



<br/>

### 处理：

**字典：** 将大写的英文单词转化为小写的单词，同时把字母的读音改成大写。为了方便区分字母和单词的读音

**文本：**

| 转化前  | 转化后  |
| ------- | ------- |
| ":"     | ","     |
| ";"     | ","     |
| "("/")" | " "     |
| "["/"]" | " "     |
| "-"     | " "     |
| "'s"    | " 's"   |
| "'ll"   | " will" |
| "'ve"   | " have" |
| "'m'"   | " am"   |



##### Files:

```bash
|--a.txt % 其他文本
|--cmu_dict.txt % 字典
|--LJ_metadata.txt % LJspeech文本
|--LJ_output.txt % 转化后的LJspeech文本
|--output.txt % 与a.txt相对应
|--process.py % 转化脚本
```

<br/>

##### How to use:

1. 处理LJspeech

```cmd
python process.py --mode LJ
```

  

2. 处理其他文件

```cmd
python process.py --mode text --text_list a.txt
```












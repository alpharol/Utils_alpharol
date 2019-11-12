from tqdm import trange
import argparse
import time

up = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
low = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
eng_pro = ["0","1","2"]
symbols = up + low + eng_pro


def write_dict():
    """
    读入CMU字典
    """
    print("------------read cmu_dict data and write them into the dict------------")
    f = open("cmu_dict.txt","r",encoding = "utf-8")
    con = f.readlines()
    f.close()
    dict = {}
    for i in trange(len(con)):
        tmp = con[i].split(" ")
        dict[tmp[0]] = "".join(tmp[1:]).replace("\n","")

    #print(dict["AARTI"])
    print("------------test data--------------")
    assert dict["aarti"] == "AA1RTIY2","the dict is not right"
    #print("the dict is right")
    return dict

def convert_LJ(dict):
    """
    将LJ-Speech的文本转化为CMU字典。
    """
    f = open("LJ_metadata.txt","r",encoding="utf-8")
    meta = f.readlines()
    f.close()
    print("------------converting the metadata to cmu_dict------------")
    for i in trange(len(meta)):
        word = ""
        tmp_meta = meta[i].split("|")[2].replace(","," , ").replace("."," . ").replace("!"," ! ").replace("?"," ? ").replace("\n","").replace(":"," , ").replace(";"," , ").replace("(","").replace(")","").replace("[","").replace("]","").replace("-"," ").replace("'s", " 's").replace("'ll", " will").replace("'ve", " have").replace("'m", " am")
        for w in tmp_meta.split(" "):
            t = w.strip()
            if len(t) != 0:
                if t in [",",".","!","?"]:
                    word = word + " " + t
                else:
                # 如果只有一个字母的话，大写就是读字母，小写就是按照单词读（a）
                    if len(t) == 1:
                        if t == "a" or t == "A":
                            word = word + " " + dict[t]
                        else:
                            word = word + " " + dict[t.upper()]
                    elif t == "'s":
                        word = word + " " + dict[t]
                    else:
                        # 如果单词不止有一个字母
                        if t[0] in low:
                            # 首字母是小写，默认单词的读音
                            if t.lower() in dict:
                                word = word + " " + dict[t.lower()]
                            else:
                                word = word + " " + t.lower()
                        elif t[0] in up and t[1] in low:
                            # 首字母是大写，第二个字母是小写，默认单词读音
                            if t.lower() in dict:
                                word = word + " " + dict[t.lower()]
                            else:
                                word = word + " " + t.lower()
                        else:
                            # 否则就默认是字母的读音
                            for k in t:
                                if k == "'":
                                    pass
                                else:
                                    word = word + " " + dict[k.upper()]
        meta[i] = bytes(meta[i].split("|")[0]+"|"+word+" % "+" \n",encoding = "utf-8")
    f = open("LJ_output.txt","wb")
    f.writelines(meta)
    f.close()



def convert_text(text_list, dict):
    f = open(text_list,"r",encoding = "utf-8")
    meta = f.readlines()
    f.close()
    for i in trange(len(meta)):
        meta[i] = meta[i].replace(","," , ").replace("."," . ").replace("!"," ! ").replace("?"," ? ").replace("|","| ").replace("\n","").replace(":"," , ").replace(";"," , ").replace("(","").replace(")","").replace("[","").replace("]","").replace("-"," ").replace("'s", " 's").replace("'ll", " will").replace("'ve", " have").replace("'m", " am")
        word = ""
        tmp_data = ""
        for n in meta[i].split(" "):
            if len(n.strip()) != 0:
                if n[-1] in ["1","2","3","4","5","#","%","$",",",".","!","?"]:
                    # 如果遇到的是中文和符号，不做处理
                    tmp_data = tmp_data + " " + n
                else:
                    # 如果遇到的是英文
                    if len(n) == 1:
                        # 如果只有一个字母，主要解决车牌号和“a”
                        if n == "a" or n == "A":
                            tmp_data = tmp_data + " " + dict[n]
                        else:
                            tmp_data = tmp_data + " " + dict[n.upper()]
                    elif n == "'s":
                        tmp_data = tmp_data + " " + dict[n]
                    else:
                        # 如果多于一个字母
                        if n[0] in low:
                            # 如果首字母是小写，那么默认单词的读音
                            if n.lower() in dict:
                                tmp_data = tmp_data + " " + dict[n.lower()]
                            else:
                                tmp_data = tmp_data + " " + n.lower()
                        elif n[0] in up and n[1] in low:
                            # 如果首字母是大写，第二个字母是小写，默认是单词的读音
                            if n.lower() in dict:
                                tmp_data = tmp_data + " " + dict[n.lower()]
                            else:
                                tmp_data = tmp_data + " " + n.lower()
                        else:
                            # 否则默认字母的读音
                            for w in n:
                                if w == "'":
                                    pass
                                else:
                                    tmp_data = tmp_data + " " + dict[w.upper()]
        if tmp_data[-1].strip()[-1] in symbols:
            tmp_data = tmp_data + " " + "%"
        meta[i] = bytes(tmp_data + "\n",encoding = "utf-8").lstrip()
    f = open("output.txt","wb")
    f.writelines(meta)
    f.close()


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--mode",default="text",help="accept mode:'LJ' for LJspeech; 'text' for normal text")
    parser.add_argument("--text_list",default="text.txt")
    args = parser.parse_args()
    
    text_list = args.text_list
    dict = write_dict()

    if args.mode == "text":
        convert_text(text_list, dict)
    else:
        convert_LJ(dict)



if __name__ == "__main__":
    main()


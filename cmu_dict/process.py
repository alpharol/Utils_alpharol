from tqdm import trange
import argparse
import time

symbols = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z","0","1","2"]

def write_dict():
    print("read cmu_dict data and write them into the dict")
    f = open("cmu_dict.txt","r",encoding = "utf-8")
    con = f.readlines()
    f.close()
    dict = {}
    for i in trange(len(con)):
        tmp = con[i].split(" ")
        dict[tmp[0]] = "".join(tmp[1:]).replace("\n","")

    #print(dict["AARTI"])
    print("------------test data--------------")
    assert dict["AARTI"] == "AA1RTIY2","the dict is not right"
    print("the dict is right")
    return dict

def convert_LJ(dict):
    ###read metadata.txt
    f = open("LJ_metadata.txt","r")
    meta = f.readlines()
    f.close()
    print("------------converting the metadata to cmu_dict------------")
    for i in trange(len(meta)):
        word = ""
        tmp_meta = meta[i].split("|")[2].upper().replace(","," , ").replace("."," . ").replace("!"," ! ").replace("?"," ? ").replace("\"","").replace("\'","").replace("\n","").replace(":"," , ").replace(";"," , ")
        for w in tmp_meta.split(" "):
            if w in dict.keys():
                word = word + " " + dict[w]
            else:
                word = word + " " + w
        if word[-2] in [",",".","!","?"]:
            word = word[:-2] + " % " + word[-2]
        else:
            word = word + " % . "
        meta[i] = bytes(meta[i].split("|")[0]+"|"+word+" \n",encoding = "utf-8")

    f = open("LJ_output.txt","wb")
    f.writelines(meta)
    f.close()



def convert_text(text_list, dict):
    f = open(text_list,"r")
    meta = f.readlines()
    f.close()
    for i in trange(len(meta)):
        meta[i] = meta[i].replace(","," , ").replace("."," . ").replace("!"," ! ").replace("?"," ? ").replace("|","| ").replace("\n","")
        word = ""
        tmp_data = ""
        for n in meta[i].split(" "):
            if len(n.strip()) != 0:
                if n[-1] in ["1","2","3","4","5","#","%","$",",",".","!","?"]:
                    tmp_data = tmp_data + " " + n
                else:
                    tmp_data = tmp_data + " " + n.upper()
        for w in tmp_data.split(" "):
            if w in dict.keys(): 
                word = word + " " + dict[w]
            else:
                word = word + " " + w
		if word[-1].strip()[-1] in symbols:
		    word = word + " " + "."
        meta[i] = bytes(word + "\n",encoding = "utf-8").lstrip()
    f = open("output.txt","wb")
    f.writelines(meta)
    f.close()


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--mode",default="LJ",help="accept mode:LJ for LJspeech; text for normal text")
	parser.add_argument("--text_list",default="text.txt")
    args = parser.parse_args()
    
	text_list = args.text_list
    dict = write_dict()
	
    if args.mode == "LJ":
        convert_LJ(dict)
    else:
        convert_text(text_list, dict)


if __name__ == "__main__":
    main()


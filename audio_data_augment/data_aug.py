import os
import subprocess
from tqdm import trange
import random
import shutil

chanxian_wav_path = "chanxian_15230_v4/wavs/"
chepai_wav_path = "chepai_1758/wavs/"
output_path = "output/"
number = 10000 ##句子数量

if os.path.exists(output_path):
    shutil.rmtree(output_path)

os.mkdir(output_path)

chanxian_filenames = os.listdir(chanxian_wav_path)
chepai_filenames = os.listdir(chepai_wav_path)

def concate_wav_end(chanxian,chepai):
    """车牌数据放在产险数据之后"""
    cmd = "sox /nfsc/cyx/data/chanxian_15230_v4/wavs/{} /nfsc/cyx/data/chepai_1758/wavs/{} /nfsc/cyx/data/output/{}_{}".format(chanxian,chepai,chanxian[:-4],chepai)
    subprocess.call(cmd,shell=True)

def concate_wav_front(chepai,chanxian):
    """车牌数据放在产险数据之后"""
    cmd = "sox /nfsc/cyx/data/chepai_1758/wavs/{} /nfsc/cyx/data/chanxian_15230_v4/wavs/{} /nfsc/cyx/data/output/{}_{}".format(chepai,chanxian,chepai[:-4],chanxian)
    subprocess.call(cmd,shell=True)


f = open("chanxian_15230_v4/chanxian_15230.pinyin","r")
con_1 = f.readlines()
f.close()

chanxian_text_dict = {}
for i in range(len(con_1)):
    chanxian_text_dict[con_1[i].split("|")[0]] = con_1[i].split("|")[1].replace("\n","")

f = open("chepai_1758/chepai_1758.pinyin","r")
con_2 = f.readlines()
f.close()

chepai_text_dict = {}
for i in range(len(con_2)):
    chepai_text_dict[con_2[i].split("|")[0]] = con_2[i].split("|")[1].replace("\n","")


text = []

for i in trange(number):
    tmp_chanxian = random.choice(chanxian_filenames)
    tmp_chepai = random.choice(chepai_filenames)

    if i%2 == 0:
        concate_wav_end(tmp_chanxian,tmp_chepai)
        tmp_text = "{}_{}".format(tmp_chanxian[:-4],tmp_chepai[:-4])+"|"+chanxian_text_dict[tmp_chanxian[:-4]].replace("% 。","").replace("% ？","").replace("% ！","")+chepai_text_dict[tmp_chepai[:-4]]
        text.append(tmp_text+"\n")
    else:
        concate_wav_front(tmp_chepai,tmp_chanxian)
        tmp_text = "{}_{}".format(tmp_chepai[:-4]),tmp_chanxian[:-4])+"|"+chepai_text_dict[tmp_chepai[:-4]].replace("% 。","")+chanxian_text_dict[tmp_chanxian[:-4]]
        text.append(tmp_text+"\n")

    chanxian_filenames.remove(tmp_chanxian)

text[-1].replace("\n","")

for i in range(len(text)):
    text[i] = bytes(text[i],encoding = "utf-8")

f = open("output_text.txt","wb")
f.writelines(text)
f.close()


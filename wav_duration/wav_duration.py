"""获取音频长度，并按照音频长度排序"""
import os
import librosa

path = "wavs/"

filenames = os.listdir(path)
print(len(filenames))

whole_list = []

for i in range(len(filenames)):
    t_list = []
    tmp = os.path.join(path,filenames[i])
    t_list.append(tmp)
    d = librosa.get_duration(filename =  tmp,sr = 22050)
    t_list.append(d)
    whole_list.append(t_list)

ans = sorted(whole_list,key = lambda x:x[1])

print(ans)

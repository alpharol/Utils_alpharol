import re
from tqdm import trange




def read_ass_file(ass_name):
    # function: read the ass file into python
    # input: filename
    # output: 
    f_ass = open(ass_name,'r',encoding="utf-16-le")
    subtitle = f_ass.readlines()
    f_ass.close()
    return subtitle

def find_event(subtitle):
    # function: find the beginning of the [Event]
    # input: subtitle
    # output: event
    new_subtitle = []
    for i in range(len(subtitle)):
        if "[Events]" in subtitle[i]:
            print("[Events]:from {}th line".format(i+1))
            print("\n")
            new_subtitle = subtitle[i:]
            break
    return new_subtitle

def get_format(new_subtitle):
    # function: get the structure of the event
    #exzample: Layer, Start, End, Style, Name, MarginL, MarginR, MarginV, Effect, Text  
    # input: new_subtitle
    # output: text_num, i.e. the index of Text in the format
    text_num = -9999
    if "Format" in new_subtitle[1]:
        subtitle_format = new_subtitle[1].split(":")[1].split(",")
        # strip the space and "\n"
        for i in range(len(subtitle_format)):
            subtitle_format[i] = subtitle_format[i].strip()
        if "Text" in subtitle_format:
            text_num = subtitle_format.index("Text")
        print("The subtitle structure is {}".format(subtitle_format))
    else:
        print("the structrue of the subtitle can not be processed by this py file")
    return text_num

def get_time_and_text(new_subtitle, text_num):
    time_text = []
    for i in range(2, len(new_subtitle)-1):
        if "".join(new_subtitle[i].split(",")[text_num:])[0] != "{":
            start = new_subtitle[i].split(",")[1]
            end = new_subtitle[i].split(",")[2]
            text = "".join(new_subtitle[i].split(",")[text_num:])
            # the information out of the {} is what we need
            p = re.sub(u"\\(.*?\\)|\\{.*?}|\\[.*?]", "", text)
            #print('p:{}'.format(p))
            # whether the subtitle is bi-languange
            if "\\N" in p:
                language_a = p.split("\\N")[0]
                language_b = p.split("\\N")[1]
            else:
                language_a = p
                language_b = ""
            if type(language_a) is str and type(language_b) is str:
                pass
            else:
                print('第{}句字幕不是str格式'.format(i))
                print('a:{}'.format(language_a))
                print('b:{}'.format(language_b))
            time_text.append([str(i), "{} --> {}".format(start, end), language_a, language_b, "\n"])
    #print(time_text)
    return time_text

def get_srt_subtitle(time_text):
    srt_subtitle = []
    print("Preparing the srt subtitle...")
    for i in trange(len(time_text)):
        srt_subtitle.append("\n".join(time_text[i]))
    print("\n")
    return srt_subtitle
    
def write_srt(srt_name, srt_subtitle):
    #using gbk for srt

    f_srt = open(srt_name,'w',encoding="gbk")
    f_srt.writelines(srt_subtitle)
    f_srt.close()


def main():
    ass_name = "S03E13.ass"
    srt_name = ass_name.split(".")[0] + ".srt"
    subtitle = read_ass_file(ass_name)
    new_subtitle = find_event(subtitle)
    
    if new_subtitle == []:
        print("Attention!!!!!!")
        print("There is no Event in ass file, please check the file")
        
    text_num = get_format(new_subtitle)
    print("Text is the {}th of the event".format(text_num+1))
    if text_num == -9999:
        print("Attention!!!!")
        print("There is no format in event!")
  
    time_text = get_time_and_text(new_subtitle, text_num)        
    srt_subtitle = get_srt_subtitle(time_text)
    print("The content of srt is finished")
    
    write_srt(srt_name, srt_subtitle)
    print("Done! You can find {}".format(srt_name))



if __name__ == "__main__":
    main()



import random

provinces = list("京津沪渝冀豫云辽黑湘皖鲁新苏浙赣鄂桂甘晋蒙陕吉闽贵粤青藏川宁琼使领")
zimu = list("ABCDEFGHJKLMNPQRSTUVWXYZ")
shuzi = list("1234567890")
five_suffix = list("挂学警港澳")
# 我们认为车牌中数字字母的比例使2：1，可以自行修改
houxuan = list("ABCDEFGHJKLMNPQRSTUVWXYZ" + "1234567890" * 6)

##########################################
##################正常车牌#################
##########################################

# 规则：省份（或者特殊前缀）简称+字母（表示地区）+5位数字字母混合

i = 0
ordinary = []
while i < 500:
    province = random.choice(provinces)
    province_char = random.choice(zimu)
    last_five_char = "".join(random.sample(houxuan, 5))
    tmp = "车牌号是{}{}{}".format(province, province_char, last_five_char)
    ordinary.append(tmp+"\n")
    i = i + 1

# print(ordinary)
# print(i)


##########################################
##################挂学警港澳################
##########################################

# 规则：省份（或者特殊前缀）简称+字母（表示地区）+4位数字字母混合+挂学警港澳

guaxue = []
while i < 600:
    province = random.choice(provinces)
    province_char = random.choice(zimu)
    last_five_char = "".join(random.sample(houxuan, 4))
    last_chi = random.choice(five_suffix)
    tmp = "车牌号是{}{}{}{}".format(province, province_char, last_five_char, last_chi)
    guaxue.append(tmp+"\n")
    i = i + 1
# print(guaxue)
# print(i)


##########################################
##################新能源小型车##############
##########################################

# 规则：省份（或者特殊前缀）简称+字母（城市）+D/F+字母或者数字（1位）+4位数字

DF = ["D", "F"]
clean_energy_mini = []
while i < 800:
    province = random.choice(provinces)
    province_char = random.choice(zimu)
    df = random.choice(DF)
    one_char = random.choice(zimu + shuzi)
    last_four_num = "".join(random.sample(shuzi, 4))
    tmp = "车牌号是{}{}{}{}{}".format(province, province_char, df, one_char, last_four_num)
    clean_energy_mini.append(tmp+"\n")
    i = i + 1

# print(clean_energy_mini)
# print(i)


##########################################
##################新能源大型车##############
##########################################

# 规则：省份（或者特殊前缀）简称+字母（城市）+5位数字+D/F

DF = ["D", "F"]
clean_energy_large = []
while i < 1000:
    province = random.choice(provinces)
    province_char = random.choice(zimu)
    five_num = "".join(random.sample(shuzi, 5))
    df = random.choice(DF)
    tmp = "车牌号是{}{}{}{}".format(province, province_char, five_num, df)
    clean_energy_large.append(tmp+"\n")
    i = i + 1

##########################################
##################新军车车牌###############
##########################################

# 两位字母 + 5位数字

army = []
while i < 1050:
    two_zimu = "".join(random.sample(zimu, 2))
    five_num = "".join(random.sample(shuzi, 5))
    tmp = "车牌号是{}{}".format(two_zimu, five_num)
    army.append(tmp+"\n")
    i = i + 1

chepai = ordinary + guaxue + clean_energy_mini + clean_energy_large + army
chepai[-1] = chepai[-1].replace("\n","")

f = open("chepai.txt","w",encoding="UTF-8")
f.writelines(chepai)
f.close()

########################################################
#####                   计数排序                    #####
########################################################

def jishu(nums, order=1):
    max_num = max(nums)
    min_num = min(nums)
    extra = [0] * (max_num - min_num + 1)
    for n in nums:
        extra[n - min_num] = extra[n - min_num] + 1

    result = []
    for i in range(len(extra)):
        if extra[i] != 0:
            result = result + ([min_num + i] * extra[i])

    if order == 1:
        return result
    else:
        return result[::-1]


test = [-2, 4, 6, 9, 0, 76, 21, 87, 65, 43, 32]
print(jishu(test))
print(jishu(test,0))


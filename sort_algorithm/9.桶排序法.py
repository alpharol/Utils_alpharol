########################################################
#####                   桶排序                      #####
########################################################

def charu(nums, order=1):
    # 第一个数不动，从第二个数开始比较
    for i in range(1, len(nums)):
        j = i - 1
        tmp = nums[i]  # 记录本次待比较的词语
        while j >= 0:
            if tmp < nums[j]:
                nums[j + 1] = nums[j]
                nums[j] = tmp
                j = j - 1
            else:
                break
    if order == 1:
        return nums
    else:
        return nums[::-1]


def tongpai(nums, n, order=1):
    max_num = max(nums)
    min_num = min(nums)
    step = (max_num + 0.1 - min_num) / int(n)
    tong = [[] for _ in range(n)]
    for i in range(len(nums)):
        tong[int((nums[i] - min_num) / step)].append(nums[i])
    result = []
    for k in range(n):
        tong[k] = charu(tong[k])
        result = result + tong[k]

    if order == 1:
        return result
    else:
        return result[::-1]


nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10.1, 10.2, 100.3]
print(tongpai(nums, 10))
print(tongpai(nums, 10, 0))

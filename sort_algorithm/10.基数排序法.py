########################################################
#####                   基数排序                    #####
########################################################

def radix_sort(nums, order=1):
    k = len(str(max(nums)))  # 最大的数的位数
    for i in range(k):
        tong = [[] for _ in range(10)]
        for num in nums:
            tong[int(num / (10 ** i)) % 10].append(num)  # 获取当前排序位数上的数字
        #print(tong)
        nums = []
        for zitong in tong:
            nums = nums + zitong
    if order == 1:
        return nums
    else:
        return nums[::-1]


nums = [1, 3, 5, 7, 9, 11, 0, 2, 100, 102, 103, 98, 78]
print(radix_sort(nums,1))
print(radix_sort(nums,0))
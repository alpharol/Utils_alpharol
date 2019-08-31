########################################################
#####                  快速排序                     #####
########################################################

def partition(nums, low, high):
    i = low - 1  # 如果直接从第一个开始的话，那么第一个元素将无法参与排序
    flag = nums[high]  # 我们取最后一个数作为比较的基准
    for j in range(low, high):
        if nums[j] <= flag:
            i = i + 1
            nums[i], nums[j] = nums[j], nums[i]
    nums[i + 1], nums[high] = nums[high], nums[i + 1]
    return i + 1


# 快速排序函数
def quick_Sort(nums, low, high, order=1):
    if low < high:
        pi = partition(nums, low, high)
        quick_Sort(nums, low, pi - 1)
        quick_Sort(nums, pi + 1, high)
    if order == 1:
        return nums
    else:
        return nums[::-1]


nums = [21, 52, 56, 8, 9, 7, 4, 1, 0, 2, 6]
print(quick_Sort(nums, 0, len(nums) - 1))
print(quick_Sort(nums, 0, len(nums) - 1, 0))

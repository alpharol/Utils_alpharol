########################################################
#####                   堆排序                      #####
########################################################

def heap_adjust(nums, start_index, end_index):
    i = start_index
    j = 2 * i
    while j <= end_index:
        if (j < end_index) and (nums[j] < nums[j + 1]):
            j = j + 1
        if nums[i] < nums[j]:
            nums[i],nums[j] = nums[j],nums[i]
            i = j
            j = 2 * i
        else:
            break

def heap_sort(nums,order=1):
    nums.insert(0,-987654321)
    nums_length = len(nums) - 1
    parent = int(nums_length / 2)
    for i in range(parent):
        heap_adjust(nums, parent - i, nums_length)

    for i in range(nums_length - 1):
        nums[1],nums[nums_length-i] = nums[nums_length-i],nums[1]
        heap_adjust(nums, 1, nums_length - i - 1)
    if order == 1:
        return nums[1:]
    else:
        return nums[1:][::-1]


nums = [1,4,3,2,9,12,23,54,76,32]

#print(heap_sort(nums))
print(heap_sort(nums,0))



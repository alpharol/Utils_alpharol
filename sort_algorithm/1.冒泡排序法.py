########################################################
#####                  冒泡排序                     #####
########################################################

def maopao(nums,order = 1):
    """
    如果order为1的话，我们默认从小到大排序；
    如果order为0的话，我们从大到小排序；
    """
    for i in range(len(nums)-1):  #如果有n个数，那么需要遍历n-1次，每次遍历的循环次数减1
        for j in range(len(nums)-1-i):
            if nums[j] > nums[j+1]:
                nums[j],nums[j+1] = nums[j+1],nums[j]
    if order == 1:
        return nums
    else:
        return nums[::-1]

print(maopao([2,3,4,1,5]))
print(maopao([2,3,4,1,5],1))
print(maopao([2,3,4,1,5],0))
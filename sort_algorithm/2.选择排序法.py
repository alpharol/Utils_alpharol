########################################################
#####                  选择排序                     #####
########################################################

def xuanze(nums, order=1):
    for i in range(len(nums)-1):
        #tmp表示记录最小值的序号，初始状态是为排序序列的首位
        tmp = i  
        for j in range(i+1,len(nums)):
            if nums[j]<nums[tmp]:  
                #找到未排序序列的最小值序号
                tmp = j   
        #如果最小值序号不等于初始序列序号，那么交换二者的位置，保证最小值在最前面
        if tmp != i:  
            nums[i],nums[tmp] = nums[tmp],nums[i]
    #我们默认是从小到大排列，如果order不等于1，我们从大到小排列
    if order == 1:
        return nums
    else:
        return nums[::-1]
    
print(xuanze([12,1,34,14,56,23,14,6,7,8,0,43,76]))
print(xuanze([12,1,34,14,56,23,14,6,7,8,0,43,76],1))
print(xuanze([12,1,34,14,56,23,14,6,7,8,0,43,76],0))
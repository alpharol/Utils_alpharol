########################################################
#####                  希尔排序                     #####
########################################################

def xier(nums,order=1):
    step = len(nums)//2 #设定初始步长
    while step != 0:    #当step不为0的时候就需要一直循环
        for i in range(step,len(nums)):
             while i>=step and nums[i] < nums[i-step]:
                 nums[i-step],nums[i] = nums[i],nums[i-step]
                 i = i-step
        step = step//2
    if order == 1:
        return nums
    else:
        return nums[::-1]
    
    
    
print(xier([21,32,43,54,65,76,87,98,1,2,3,4,5]))
print(xier([21,32,43,54,65,76,87,98,1,2,3,4,5],1))
print(xier([21,32,43,54,65,76,87,98,1,2,3,4,5],0))
########################################################
#####                  插入排序                     #####
########################################################

def charu(nums,order = 1):
    #第一个数不动，从第二个数开始比较
    for i in range(1,len(nums)):
        j=i-1
        tmp = nums[i] #记录本次待比较的词语
        while j >= 0:
            if tmp < nums[j]:
                nums[j+1] = nums[j]
                nums[j] = tmp
                j = j-1
            else:
                break
    if order == 1:
        return nums
    else:
        return nums[::-1]

print(charu([12,23,34,45,56,87,94,0,9,6,2,7]))
print(charu([12,23,34,45,56,87,94,0,9,6,2,7],1))
print(charu([12,23,34,45,56,87,94,0,9,6,2,7],0))

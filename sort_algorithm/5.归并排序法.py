########################################################
#####                  归并排序                     #####
########################################################

def merge(num_1, num_2):
    result = []
    i, j = 0, 0
    while i < len(num_1) and j < len(num_2):
        if num_1[i] < num_2[j]:
            result.append(num_1[i])
            i = i + 1
        else:
            result.append(num_2[j])
            j = j + 1
    result = result + num_1[i:] + num_2[j:]
    return result


def guibing(nums, order=1):
    if len(nums) == 0:
        return print("Please input a valid list")
    elif len(nums) == 1:
        return nums
    else:
        middle = len(nums) // 2
        left = guibing(nums[:middle])
        right = guibing(nums[middle:])
        final_result = merge(left, right)
    if order == 1:
        return final_result
    else:
        return final_result[::-1]


nums = [11, 23, 43, 0, 8, 7, -8, -1, 14, 87, 34]
print(guibing(nums))
print(guibing(nums, order=1))
print(guibing(nums, order=0))

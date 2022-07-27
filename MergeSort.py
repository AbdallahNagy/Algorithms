#Merge Sort Algorithm
def merge_sort(unsorted_list):
    if len(unsorted_list) <=1:
        return unsorted_list

    #Find the middle point and divide it
    middle = len(unsorted_list) // 2

    #split the list by half
    left_list = unsorted_list[:middle]
    right_list = unsorted_list[middle:]

    #do it untill you reach to one ele in a list
    left_list = merge_sort(left_list)
    right_list = merge_sort(right_list)

    return list(merge(left_list, right_list))

def merge(left_half, right_half):
    res = []
    while len(left_half) != 0 and len(right_half) != 0:
        if left_half < right_half:
            res.append(left_half[0])
            left_half.remove(left_half[0])
        else:
            res.append(right_half[0])
            right_half.remove(right_half[0])
    
    if len(left_half) == 0:
        res = res + right_half
    else:
        res = res + left_half

    return res

arr = [10, 50, 40, 20, 30]
print(merge_sort(arr))

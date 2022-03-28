def findMaxSubArray(array, low, end):
    if(low >= end):
        raise Exception
    elif end - low == 1:
        return (array, low, end, array[low])
    middle = int((low + end - 1) / 2)

    leftResult = findMaxSubArray(array, low, middle + 1)
    middleResult = findMaxCrossingSubArray(array, low, middle, end)
    rightResult = findMaxSubArray(array, middle + 1, end)
    if leftResult[3] > middleResult[3]:
        if leftResult[3] > rightResult[3]:
            return leftResult
        else:
            return rightResult
    if middleResult[3] > rightResult[3]:
        return middleResult
    else:
        return rightResult
        

        

def findMaxCrossingSubArray(array, low, mid, end):
    if low == end -1:
        return (array[low : end], low, end, array[low])
    i = mid
    tempSum = 0
    max_left_sum = None
    while i >= low:
       tempSum += array[i] 
       if max_left_sum == None or max_left_sum < tempSum:
           max_left_sum = tempSum
           max_left_index = i
       i -= 1

    i = mid + 1
    tempSum = 0
    max_right_sum = 0
    max_right_index = mid
    while i < end:
        tempSum += array[i]
        if max_right_sum < tempSum:
            max_right_sum = tempSum
            max_right_index = i
        i += 1

    return (array[max_left_index: max_right_index + 1], max_left_index, max_right_index + 1, max_left_sum + max_right_sum)



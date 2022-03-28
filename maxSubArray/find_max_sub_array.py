def find_max_sub_array(array, low, end):
    if low >= end:
        raise Exception
    elif end - low == 1:
        return array, low, end, array[low]
    middle = int((low + end - 1) / 2)

    left_result = find_max_sub_array(array, low, middle + 1)
    middle_result = find_max_crossing_sub_array(array, low, middle, end)
    right_result = find_max_sub_array(array, middle + 1, end)
    if left_result[3] > middle_result[3]:
        if left_result[3] > right_result[3]:
            return left_result
        else:
            return right_result
    if middle_result[3] > right_result[3]:
        return middle_result
    else:
        return right_result


def find_max_crossing_sub_array(array, low, mid, end):
    if low == end - 1:
        return array[low: end], low, end, array[low]
    i = mid
    temp_sum = 0
    max_left_sum = None
    while i >= low:
        temp_sum += array[i]
        if max_left_sum is None or max_left_sum < temp_sum:
            max_left_sum = temp_sum
            max_left_index = i
        i -= 1

    i = mid + 1
    temp_sum = 0
    max_right_sum = 0
    max_right_index = mid
    while i < end:
        temp_sum += array[i]
        if max_right_sum < temp_sum:
            max_right_sum = temp_sum
            max_right_index = i
        i += 1

    return (
        array[max_left_index: max_right_index + 1], max_left_index, max_right_index + 1, max_left_sum + max_right_sum)

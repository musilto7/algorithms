def merge_sort(array):
    _merge_sort(array, 0, len(array))


def _merge_sort(array, start, end):
    middle = int((end + start) / 2)
    if middle - start > 1:
        _merge_sort(array, start, middle)
    if end - middle > 1:
        _merge_sort(array, middle, end)
    merge(array, start, middle, end)


def merge(array, start, middle, end):
    temp_array = [*range(0, end - start)]
    temp_array_index = 0
    temp_middle = middle
    temp_start = start
    while temp_array_index + start < end:
        if temp_start < middle:
            if temp_middle < end and array[temp_start] > array[temp_middle]:
                retrieved_value = array[temp_middle]
                temp_middle += 1
            else:
                retrieved_value = array[temp_start]
                temp_start += 1
        else:
            retrieved_value = array[temp_middle]
            temp_middle += 1

        temp_array[temp_array_index] = retrieved_value
        temp_array_index += 1

    for arrayIndex in range(start, end):
        array[arrayIndex] = temp_array[arrayIndex - start]

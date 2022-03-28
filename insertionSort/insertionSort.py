def insertion_sort(array):
    for index in range(1, len(array)):
        value_for_swap = array[index]
        index2 = index
        while index2 - 1 >= 0 and array[index2 - 1] > value_for_swap:
            array[index2] = array[index2 - 1]
            index2 -= 1
        array[index2] = value_for_swap
    return array

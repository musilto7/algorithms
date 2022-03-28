
def insertionSort(array):
    for index in range(1, len(array)):
        valueForSwap = array[index]
        index2 = index
        while index2 - 1 >= 0 and array[index2 -1] > valueForSwap:
            array[index2] = array[index2 - 1]
            index2 -= 1
        array[index2] = valueForSwap
    return array

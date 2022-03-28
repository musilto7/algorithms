
def bubble_sort(array):
    for i in range(0, len(array)):
        for itemIndex in range(1, len(array)):
            previousItemIndex = itemIndex - 1
            if array[previousItemIndex] > array[itemIndex]:
                tempValue = array[previousItemIndex]
                array[previousItemIndex] = array[itemIndex]
                array[itemIndex] = tempValue
            

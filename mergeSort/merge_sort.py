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
    tempArray = [*range(0, end - start)]
    tempArrayIndex = 0
    tempMiddle = middle
    tempStart = start
    while tempArrayIndex + start < end:
        if tempStart < middle:
            if tempMiddle < end and array[tempStart] > array[tempMiddle]:
                retrievedValue = array[tempMiddle] 
                tempMiddle += 1
            else:
                retrievedValue = array[tempStart]
                tempStart += 1
        else:
            retrievedValue = array[tempMiddle]
            tempMiddle += 1

        tempArray[tempArrayIndex] = retrievedValue
        tempArrayIndex += 1

    for arrayIndex in range(start, end):
        array[arrayIndex] = tempArray[arrayIndex - start]

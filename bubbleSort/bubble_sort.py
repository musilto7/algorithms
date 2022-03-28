
def bubble_sort(array):
    for i in range(0, len(array)):
        for item_index in range(1, len(array)):
            previous_item_index = item_index - 1
            if array[previous_item_index] > array[item_index]:
                temp_value = array[previous_item_index]
                array[previous_item_index] = array[item_index]
                array[item_index] = temp_value
            

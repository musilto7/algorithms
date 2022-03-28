from merge_sort import merge
from merge_sort import merge_sort

def test_merge_with_empty_input():
    inputArray = []
    merge(inputArray, 0, 0, 0)
    assert inputArray == []

def test_merge_with_non_empty_input():
    inputArray = [1]
    merge(inputArray, 0, 1, 1)
    assert inputArray == [1]

def test_merge_with_non_trivial_input():
    inputArray = [2, 1]
    merge(inputArray, 0, 1, 2)
    assert inputArray == [1, 2]

def test_merge_with_three_numbers_input():
    inputArray = [2, 3, 1]
    merge(inputArray, 0, 2, 3)
    assert inputArray == [1, 2, 3]

def test_merge_with_three_numbers_input_diferent_bounds():
    inputArray = [3, 1, 2]
    merge(inputArray, 0, 1, 3)
    assert inputArray == [1, 2, 3]


def test_merge_input_with_partial_bounds():
    inputArray = [11, 2, 3, 1, -1]
    merge(inputArray, 1, 3, 4)
    assert inputArray == [11, 1, 2, 3, -1]

def test_mergeSort_with_empty_input():
    inputArray = []
    merge_sort(inputArray)
    assert inputArray == []

def test_mergeSort_with_trivial_input():
    inputArray = [1]
    merge_sort(inputArray)
    assert inputArray == [1]

def test_mergeSort_with_non_trivial_input():
    inputArray = [2, 1, 0]
    merge_sort(inputArray)
    assert inputArray == [0, 1, 2]

def test_mergeSort_with_some_advanced_input():
    inputArray = [2, 1, -1, -6, 12, 11, 4, 5, 1, 42, 18]
    merge_sort(inputArray)
    assert inputArray == [-6, -1, 1, 1, 2, 4, 5, 11, 12, 18, 42]

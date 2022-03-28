from merge_sort import merge
from merge_sort import merge_sort


def test_merge_with_empty_input():
    input_array = []
    merge(input_array, 0, 0, 0)
    assert input_array == []


def test_merge_with_non_empty_input():
    input_array = [1]
    merge(input_array, 0, 1, 1)
    assert input_array == [1]


def test_merge_with_non_trivial_input():
    input_array = [2, 1]
    merge(input_array, 0, 1, 2)
    assert input_array == [1, 2]


def test_merge_with_three_numbers_input():
    input_array = [2, 3, 1]
    merge(input_array, 0, 2, 3)
    assert input_array == [1, 2, 3]


def test_merge_with_three_numbers_input_different_bounds():
    input_array = [3, 1, 2]
    merge(input_array, 0, 1, 3)
    assert input_array == [1, 2, 3]


def test_merge_input_with_partial_bounds():
    input_array = [11, 2, 3, 1, -1]
    merge(input_array, 1, 3, 4)
    assert input_array == [11, 1, 2, 3, -1]


def test_merge_sort_with_empty_input():
    input_array = []
    merge_sort(input_array)
    assert input_array == []


def test_merge_sort_with_trivial_input():
    input_array = [1]
    merge_sort(input_array)
    assert input_array == [1]


def test_merge_sort_with_non_trivial_input():
    input_array = [2, 1, 0]
    merge_sort(input_array)
    assert input_array == [0, 1, 2]


def test_merge_sort_with_some_advanced_input():
    input_array = [2, 1, -1, -6, 12, 11, 4, 5, 1, 42, 18]
    merge_sort(input_array)
    assert input_array == [-6, -1, 1, 1, 2, 4, 5, 11, 12, 18, 42]

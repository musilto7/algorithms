from bubble_sort import bubble_sort


def test_empty_input():
    input_array = []
    bubble_sort(input_array)
    assert input_array == []


def test_non_trivial_input():
    input_array = [8, 1, 0, 6, 12, 67, 42]
    bubble_sort(input_array)
    assert input_array == [0, 1, 6, 8, 12, 42, 67]

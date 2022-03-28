
from bubble_sort import bubble_sort

def test_empty_input():
	input = []
	bubble_sort(input)
	assert input == []

def test_non_trivial_input():
    input = [8, 1, 0, 6, 12, 67, 42]
    bubble_sort(input)
    assert input == [0, 1, 6, 8, 12, 42, 67]

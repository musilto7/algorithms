from findMaxSubArray import find_max_crossing_sub_array
from findMaxSubArray import find_max_sub_array
import pytest


def test_find_max_sub_array_for_empty_array():
    with pytest.raises(Exception):
        find_max_sub_array([], 0, 0)


def test_find_max_sub_array_for_one_element_array():
    result = find_max_sub_array([-5], 0, 1)
    assert result == ([-5], 0, 1, -5)


def test_find_max_sub_array_for_non_trivial_array():
    result = find_max_sub_array([2, -1, 4, -3, -2, 6, 1, -3, 1, 1], 0, 10)
    assert result == ([6, 1], 5, 7, 7)


def test_find_max_crossing_sub_array_for_one_element_array():
    result = find_max_crossing_sub_array([3], 0, 0, 1)
    assert result == ([3], 0, 1, 3)


def test_find_max_crossing_sub_array_for_two_element_array():
    result = find_max_crossing_sub_array([6, 4, -1, 8], 1, 1, 3)
    assert result == ([4], 1, 2, 4)

    result = find_max_crossing_sub_array([6, 4, 1, 8], 1, 1, 3)
    assert result == ([4, 1], 1, 3, 5)

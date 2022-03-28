
from findMaxSubArray import findMaxCrossingSubArray
from findMaxSubArray import findMaxSubArray
import pytest

def test_findMaxSubArray_for_emty_array():
    with pytest.raises(Exception):
        findMaxSubArray([], 0, 0) 

def test_findMaxSubArray_for_one_element_array():
    result = findMaxSubArray([-5], 0, 1)
    assert result == ([-5], 0, 1, -5)

def test_findMaxSubArray_for_non_trivial_array():
    result = findMaxSubArray([2,-1, 4, -3, -2, 6, 1, -3, 1, 1], 0, 10)
    assert result == ([6, 1], 5, 7, 7)

def test_findMaxCrossingSubArray_for_one_element_array():
    result = findMaxCrossingSubArray([3], 0, 0, 1)
    assert result == ([3], 0, 1, 3)

def test_findMaxCrossingSubArray_for_two_element_array():
    result = findMaxCrossingSubArray([6, 4, -1, 8], 1, 1, 3) 
    assert result == ([4], 1, 2, 4)

    result = findMaxCrossingSubArray([6, 4, 1, 8], 1, 1, 3)
    assert result == ([4, 1], 1, 3, 5)


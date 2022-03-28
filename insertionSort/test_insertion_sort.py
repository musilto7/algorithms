from insertion_sort import insertion_sort


def test_empty():
    assert [] == insertion_sort([])


def test_one_value():
    assert [1] == insertion_sort([1])


def test_multiple_values():
    assert [1, 2, 3, 4, 5, 6, 7] == insertion_sort([7, 6, 2, 1, 5, 4, 3])

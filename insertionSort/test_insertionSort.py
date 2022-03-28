from insertionSort import insertionSort

def test_empty():
   assert [] == insertionSort([]) 

def test_oneValue():
    assert [1] == insertionSort([1])

def test_multipleValues():
    assert [1, 2, 3, 4, 5, 6, 7] == insertionSort([7, 6, 2, 1, 5, 4, 3])

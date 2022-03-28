from matrix import Matrix
import pytest
from matrix import join_quarters

def test_matrix_construction():
    matrix = Matrix([])

def test_matrix_add():
    matrix1 = Matrix([[1, 2], [3, 4]])
    matrix2 = Matrix([[0, 1], [3, 0]])
    assert [[1, 3], [6, 4]] == matrix1.add(matrix2).array
    assert [[1, 2], [3, 4]] == matrix1.array

def test_add_non_square_matrix():
    matrix1 = Matrix([[1, 0]])
    matrix2 = Matrix([[2, 1]])
    assert [[3, 1]] == matrix1.add(matrix2).array

def test_add_unit_matrix():
    matrix1 = Matrix([[1]])
    matrix2 = Matrix([[2]])
    assert [[3]] == matrix1.add(matrix2).array

def test_quarter_small_matrix_raises_exception():
    matrix = Matrix([[1]])
    with pytest.raises(Exception):
        matrix.quarter()

def test_quarter_matrix():
    matrix = Matrix([[0,1], [2,3]])
    quards = matrix.quarter()
    assert quards[0].array == [[0]]
    assert quards[1].array == [[1]]
    assert quards[2].array == [[2]]
    assert quards[3].array == [[3]]

def test_join_quarters():
    matrix1 = Matrix([[1]])
    matrix2 = Matrix([[2]])
    matrix3 = Matrix([[3]])
    matrix4 = Matrix([[4]])
    assert [[1, 2], [3, 4]] == join_quarters(matrix1, matrix2, matrix3, matrix4).array


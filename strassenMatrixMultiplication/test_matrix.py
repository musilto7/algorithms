from matrix import Matrix
import pytest
from matrix import _join_quarters


def test_matrix_construction():
    Matrix([])


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


def test_substract_unit_matrix():
    matrix1 = Matrix([[1]])
    matrix2 = Matrix([[2]])
    assert [[-1]] == matrix1.subtract(matrix2).array


def test_quarter_small_matrix_raises_exception():
    matrix = Matrix([[1]])
    with pytest.raises(Exception):
        matrix.quarter()


def test_quarter_matrix():
    matrix = Matrix([[0, 1], [2, 3]])
    (a11, a12, a21, a22) = matrix.quarter()
    assert a11.array == [[0]]
    assert a12.array == [[1]]
    assert a21.array == [[2]]
    assert a22.array == [[3]]


def test_join_quarters():
    matrix1 = Matrix([[1]])
    matrix2 = Matrix([[2]])
    matrix3 = Matrix([[3]])
    matrix4 = Matrix([[4]])
    assert [[1, 2], [3, 4]] == _join_quarters(matrix1, matrix2, matrix3, matrix4).array


def test_multiply_trivial_matrix():
    matrix1 = Matrix([[2]])
    matrix2 = Matrix([[2]])
    assert matrix1.multiply(matrix2).array == [[4]]


def test_multiply_non_trivial_matrix():
    matrix1 = Matrix([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]])

    matrix2 = Matrix([[2, 0, 0, 0], [0, 2, 0, 0], [0, 0, 2, 0], [0, 0, 0, 2]])
    result_matrix = matrix1.multiply(matrix2)
    assert result_matrix.array == [[2, 4, 6, 8], [10, 12, 14, 16], [18, 20, 22, 24], [26, 28, 30, 32]]

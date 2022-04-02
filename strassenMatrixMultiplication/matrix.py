class Matrix:
    def __init__(self, array):
        self.array = array

    def multiply(self, matrix):
        if self._rows() == 1:
            value = self.array[0][0] * matrix.array[0][0]
            return Matrix([[value]])
        (a11, a12, a21, a22) = self.quarter()
        (b11, b12, b21, b22) = matrix.quarter()
        s1 = b12.subtract(b22)
        s2 = a11.add(a12)
        s3 = a21.add(a22)
        s4 = b21.subtract(b11)
        s5 = a11.add(a22)
        s6 = b11.add(b22)
        s7 = a12.subtract(a22)
        s8 = b21.add(b22)
        s9 = a11.subtract(a21)
        s10 = b11.add(b12)

        p1 = a11.multiply(s1)
        p2 = s2.multiply(b22)
        p3 = s3.multiply(b11)
        p4 = a22.multiply(s4)
        p5 = s5.multiply(s6)
        p6 = s7.multiply(s8)
        p7 = s9.multiply(s10)

        c11 = p5.add(p4).subtract(p2).add(p6)
        c12 = p1.add(p2)
        c21 = p3.add(p4)
        c22 = p5.add(p1).subtract(p3).subtract(p7)

        return _join_quarters(c11, c12, c21, c22)

    def add(self, matrix):
        return self._add(matrix, 1)

    def subtract(self, matrix):
        return self._add(matrix, -1)

    def _add(self, matrix, multiplier):
        rows = self._rows()
        columns = self._columns()
        new_array = [[0 for i in range(columns)] for _ in range(rows)]
        for r in range(rows):
            for c in range(columns):
                first = (self.array[r][c])
                second = (matrix.array[r][c])
                new_array[r][c] = first + (second * multiplier)
        return Matrix(new_array)

    def quarter(self):
        rows = self._rows()
        if rows <= 1:
            raise Exception("Size of matrix has to be greater than 1")
        middle = int(rows / 2)
        start_slice = slice(0, middle)
        end_slice = slice(middle, rows)
        return [self._one_quarter(start_slice, start_slice), self._one_quarter(start_slice, end_slice),
                self._one_quarter(end_slice, start_slice), self._one_quarter(end_slice, end_slice)]

    def _one_quarter(self, row_slice, column_slice):
        temp_array = self.array[row_slice]
        for rowIndex in range(len(temp_array)):
            temp_array[rowIndex] = temp_array[rowIndex][column_slice]
            return Matrix(temp_array)

    def concat_columns(self, m2):
        row_range = range(0, self._rows())
        result = [[] for _ in row_range]
        for r in row_range:
            result[r] = self.array[r] + m2.array[r]
        return Matrix(result)

    def _rows(self):
        return len(self.array)

    def _columns(self):
        return len(self.array[0])


def _join_quarters(matrix1, matrix2, matrix3, matrix4):
    return Matrix((matrix1.concat_columns(matrix2)).array + (matrix3.concat_columns(matrix4)).array)

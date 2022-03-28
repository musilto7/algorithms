class Matrix:
    def __init__(self, array):
        self.array = array

    def add(self, matrix):
        rows = self._rows()
        columns = self._columns()
        new_array = [[0 for i in range(columns)] for _ in range(rows)]
        for r in range(rows):
            for c in range(columns):
                first = (self.array[r][c])
                second = (matrix.array[r][c])
                new_array[r][c] = first + second
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

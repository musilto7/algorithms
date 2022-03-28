class Matrix:
    def __init__(self, array):
        self.array = array

    def add(self, matrix):
        rows = self._rows() 
        columns = self._columns() 
        newArray = [[0 for i in range(columns)] for j in range(rows)]
        for r in range(rows):
            for c in range(columns):
                first = (self.array[r][c])
                second = (matrix.array[r][c])
                newArray[r][c] = first + second
        return Matrix(newArray)
        
    def quarter(self):
        rows = self._rows()
        if rows <= 1:
            raise Exception("Size of matrix has to be greater than 1")
        middle = int(rows / 2) 
        startSlice = slice(0, middle)
        endSlice = slice(middle, rows)
        return [self._one_quarter(startSlice, startSlice), self._one_quarter(startSlice, endSlice), self._one_quarter(endSlice, startSlice), self._one_quarter(endSlice, endSlice)]

    def _one_quarter(self, rowSlice, columnSlice):
        tempArray = self.array[rowSlice]
        for rowIndex in range(len(tempArray)):
            tempArray[rowIndex] = tempArray[rowIndex][columnSlice]
            return Matrix(tempArray)

    def _concat_columns(self, m2):
        rowRange = range(0, self._rows())
        result = [[] for r in rowRange]
        for r in rowRange:
            result[r] = self.array[r] + m2.array[r]
        return Matrix(result)

    def _rows(self):
        return len(self.array)

    def _columns(self):
        return len(self.array[0])

def join_quarters(m1, m2, m3, m4):
    return Matrix((m1._concat_columns(m2)).array + (m3._concat_columns(m4)).array)

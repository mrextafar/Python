def makingOneDimensionalIntoMultidimensional(rows,cols,x):
    # Разбиение одномерного листа в соответствии с размерами слагаемых матриц
    res = [[0] * cols for i in range(rows)]
    c = 0
    for i in range(rows):
        for j in range(cols):
            res[i][j] = x[c]
            c += 1
    return res
class Matrix():
    def __init__(self, matrix):
        lenghtRowList = []
        for i in range(len(matrix)):
            lenghtRowList.append(len(matrix[i]))
        l0 = len(matrix[0])
        for i in lenghtRowList:
            if i != l0:
                print("Плохая матрица")
                break
        self.matrix = matrix

    def __str__(self):
        res = ""
        for j in range(len(self.matrix)):
            res += (f"{self.matrix[j]}\n")

        return str(res)

    def __add__(self, other):
        res = []
        if len(self.matrix) != len(other.matrix) or len(self.matrix[0]) != len(other.matrix[0]):
            return print("Матрицы должны быть одинакового размера")
        for i in range(len(self.matrix)):
            for y in range(len(self.matrix[0])):
                res.append(self.matrix[i][y] + other.matrix[i][y])  # Одномерный лист

        # Превращаю в многомерный лист
        rows = len(self.matrix)
        cols = len(self.matrix[0])
        res = makingOneDimensionalIntoMultidimensional(rows, cols, res)

        return Matrix(res)

    def __sub__(self, other):
        res = []
        if len(self.matrix) != len(other.matrix) or len(self.matrix[0]) != len(other.matrix[0]):
            return print("Матрицы должны быть одинакового размера")
        for i in range(len(self.matrix)):
            for y in range(len(self.matrix[0])):
                res.append(self.matrix[i][y] - other.matrix[i][y])  # Одномерный лист

        # Превращаю в многомерный лист
        rows = len(self.matrix)
        cols = len(self.matrix[0])
        res = makingOneDimensionalIntoMultidimensional(rows, cols, res)

        return Matrix(res)

    def multiply_by_number(self, number):
        res = []
        for i in range(len(self.matrix)):
            for y in range(len(self.matrix[0])):
                res.append(self.matrix[i][y] * number) # Одномерный лист

        # Превращаю в многомерный лист
        rows = len(self.matrix)
        cols = len(self.matrix[0])
        res = makingOneDimensionalIntoMultidimensional(rows, cols, res)

        return Matrix(res)

    def __mul__(self, other):
        res = []
        rows = len(self.matrix)
        cols = len(other.matrix[0])
        for i in range(rows):
            for j in range(cols):
                res.append(0)
        if len(self.matrix) != len(other.matrix[0]) and len(self.matrix[0]) != len(other.matrix):
            return print("Длина строки первой матрицы должна быть равна длине столбца второй матрицы")
        a = 0
        for i in range(rows):
            for j in range(cols):
                temp = 0
                for k in range(len(other.matrix)):
                    temp += self.matrix[i][k] * other.matrix[k][j]
                res[a] = temp
                a += 1
                #res.append(self.matrix[i][j] * other.matrix[i][j])
        # Превращаю в многомерный лист
        res = makingOneDimensionalIntoMultidimensional(rows, cols, res)
        return Matrix(res)

    def determinant(self):
        if len(self.matrix) != len(self.matrix[0]):
            return print("Детерминировать можно только квадратные матрицы")

def multidimensional(matrix):
    if not isinstance(matrix, tuple):
        return -1
    for i in matrix:
        if isinstance(i, tuple) and len(i) > 1:
            return True
    return False

def makingOneDimensionalIntoMultidimensional(rows,cols,x):
    # Разбиение одномерного листа в соответствии с размерами слагаемых матриц
    res = [[0] * cols for i in range(rows)]
    c = 0
    for i in range(rows):
        for j in range(cols):
            res[i][j] = x[c]
            c += 1
    # Превращение матрицы списков в матрицу кортежей
    for i in range(rows):
        res[i] = tuple(res[i])
    res = tuple(res)
    return res


class Matrix():
    def __init__(self, matrix):
        if multidimensional(matrix) == True:
            #Многомерная матрица
            for i in range(len(matrix)-1):
                if len(matrix[i]) == len(matrix[i+1]):
                    #Правильная многомерная матрица
                    res = matrix
                elif len(matrix[i]) != len(matrix[i+1]):
                    #Разные размеры строк или столбцов многомерной матрицы
                    print("Плохая матрица")
                    break
        elif multidimensional(matrix) == False:
            res = matrix
        elif multidimensional(matrix) == -1:
            print("Не матрица")
        res = tuple(res)
        self.matrix = res



    def __str__(self):
        res = ""
        if multidimensional(self.matrix):
            for j in range(len(self.matrix)):
                res += (f"{self.matrix[j]}\n")
        else:
             #Одномерная матрица
             res = self.matrix

        return str(res)


    def __add__(self, other):
        x = []
        res = ()
        if len(self.matrix) == len(other.matrix):
            #Матрицы одинакого размера
            for i in range(len(self.matrix)):
                if multidimensional(self.matrix):
                    for y in range(len(self.matrix[0])):
                        x.append(self.matrix[i][y] + other.matrix[i][y])#Получаю сложение в виде одномерного листа
                else:
                    x.append(self.matrix[i] + other.matrix[i])

            if multidimensional(self.matrix):
                #Разбиение одномерного листа в соответствии с размерами слагаемых матриц
                rows = len(self.matrix)
                cols = len(self.matrix[0])
                res = makingOneDimensionalIntoMultidimensional(rows, cols, x)
            else:
                res = x
                res = tuple(res)

        res = Matrix(res)
        return res

    def __sub__(self, other):
        x = []
        res = ()

        if len(self.matrix) == len(other.matrix):
            # Матрицы одинакого размера
            for i in range(len(self.matrix)):
                if multidimensional(self.matrix):
                    for y in range(len(self.matrix[0])):
                        x.append(self.matrix[i][y] + other.matrix[i][y]*(-1))  # Получаю сложение в виде одномерного листа
                else:
                    x.append(self.matrix[i] + other.matrix[i])

            if multidimensional(self.matrix):
                # Разбиение одномерного листа в соответствии с размерами слагаемых матриц
                rows = len(self.matrix)
                cols = len(self.matrix[0])
                res = makingOneDimensionalIntoMultidimensional(rows,cols,x)
            else:
                res = x
                res = tuple(res)

        res = Matrix(res)
        return res

    def multiply_by_number(self,number):
        x = []
        res = ()
        for i in range(len(self.matrix)):
            if multidimensional(self.matrix):
                for y in range(len(self.matrix[0])):
                    x.append(self.matrix[i][y] * number)  # Получаю сложение в виде одномерного листа
            else:
                x.append(self.matrix[i] * number)

        if multidimensional(self.matrix):
            # Разбиение одномерного листа в соответствии с размерами слагаемых матриц
            rows = len(self.matrix)
            cols = len(self.matrix[0])
            res = makingOneDimensionalIntoMultidimensional(rows, cols, x)
        else:
            res = x
            res = tuple(res)

        res = Matrix(res)
        return res

    def __mul__(self,other):
        # Принимает только ixj * jxi Где i>j
        x = []
        res = ()

    #if multidimensional(self.matrix) and multidimensional(other.matrix):
        flag = True
        if not isinstance(other.matrix[0], tuple):
            n = len(other.matrix)
            flag = False
        else:
            n = len(other.matrix[0])
        if len(self.matrix) == n:
            for z in range(n):
                x.append([0] * n)
            for i in range(len(self.matrix)):
                for j in range(n):
                    for k in range(len(other.matrix)):
                        if flag:
                            x[i][j] += self.matrix[i][k] * other.matrix[k][j]
                        else:
                            x[i][j] += self.matrix[k][0] * other.matrix[k]
            res = x
            for c in range(len(res)):
                res[c] = tuple(res[c])
        # else:
        #     print("Нельзя посчитать. Матрицы должны быть типа 3х2 * 2х3")


        res = tuple(res)
        res = Matrix(res)
        return res
    #def determinant(self):

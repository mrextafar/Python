from matrix_operations import *

def OutputCheck():
    matrix23 = Matrix([[1,2,3],[4,5,6]])
    matrix31 = Matrix([[1],[2],[3]])
    matrix13 = Matrix([[1,2,3]])
    matrix33 = Matrix([[1,2,3,],[4,5,6],[7,8,9]])
    print(matrix23)
    print(matrix31)
    print(matrix13)
    print(matrix33)

#OutputCheck()

def AddCheck():
    matrix23 = Matrix([[1, 2, 3], [4, 5, 6]])
    matrix31 = Matrix([[1], [2], [3]])
    matrix13 = Matrix([[1, 2, 3]])
    matrix33 = Matrix([[1, 2, 3, ], [4, 5, 6], [7, 8, 9]])
    otherMatrix23 = Matrix([[11,12,13],[14,15,16]])
    otherMatrix31 = Matrix([[11],[12],[13]])
    otherMatrix13 = Matrix([[11, 12, 13]])
    otherMatrix33 = Matrix([[11,12,13],[14,15,16],[17,18,19]])

    print("1 = Посчитать")
    mm23 = matrix23 + otherMatrix23
    print(mm23)
    mm31 = matrix31 + otherMatrix31
    print(mm31)
    mm13 = matrix13 + otherMatrix13
    print(mm13)
    mm33 = matrix33 + otherMatrix33
    print(mm33)

    print("2 = Матрицы должны быть одинакового размера\nnone")
    mn1 = matrix23 + otherMatrix31
    print(mn1)
    mn2 = matrix23 + otherMatrix13
    print(mn2)
    mn3 = matrix23 + otherMatrix33
    print(mn3)
    mn4 = matrix31 + otherMatrix13
    print(mn4)
    mn5 = matrix31 + otherMatrix33
    print(mn5)
    mn6 = matrix13 + otherMatrix33
    print(mn6)

#AddCheck()

def SubCheck():
    matrix23 = Matrix([[1, 2, 3], [4, 5, 6]])
    matrix31 = Matrix([[1], [2], [3]])
    matrix13 = Matrix([[1, 2, 3]])
    matrix33 = Matrix([[1, 2, 3, ], [4, 5, 6], [7, 8, 9]])
    otherMatrix23 = Matrix([[9,8,7],[6,5,4]])
    otherMatrix31 = Matrix([[9],[8],[7]])
    otherMatrix13 = Matrix([[9, 8, 7]])
    otherMatrix33 = Matrix([[9,8,7],[6,5,4],[3,2,1]])

    print("1 = Посчитать")
    mm23 = matrix23 - otherMatrix23
    print(mm23)
    mm31 = matrix31 - otherMatrix31
    print(mm31)
    mm13 = matrix13 - otherMatrix13
    print(mm13)
    mm33 = matrix33 - otherMatrix33
    print(mm33)

    print("2 = Матрицы должны быть одинакового размера\nnone")
    mn1 = matrix23 - otherMatrix31
    print(mn1)
    mn2 = matrix23 - otherMatrix13
    print(mn2)
    mn3 = matrix23 - otherMatrix33
    print(mn3)
    mn4 = matrix31 - otherMatrix13
    print(mn4)
    mn5 = matrix31 - otherMatrix33
    print(mn5)
    mn6 = matrix13 - otherMatrix33
    print(mn6)

#SubCheck()

def MultiplyByNumberCheck():
    matrix23 = Matrix([[1, 2, 3], [4, 5, 6]])
    mm23 = Matrix.multiply_by_number(matrix23,2)
    print(mm23)
    matrix31 = Matrix([[1], [2], [3]])
    mm31 = Matrix.multiply_by_number(matrix23, 3)
    print(mm31)
    matrix13 = Matrix([[1, 2, 3]])
    mm13 = Matrix.multiply_by_number(matrix23, 4)
    print(mm13)
    matrix33 = Matrix([[1, 2, 3, ], [4, 5, 6], [7, 8, 9]])
    mm33 = Matrix.multiply_by_number(matrix23, 5)
    print(mm33)

#MultiplyByNumberCheck()

def MultiplyCheck():
    matrix23 = Matrix([[1, 2, 3], [4, 5, 6]])
    matrix31 = Matrix([[1], [2], [3]])
    matrix13 = Matrix([[1, 2, 3]])
    matrix33 = Matrix([[1, 2, 3, ], [4, 5, 6], [7, 8, 9]])
    otherMatrix32 = Matrix([[9, 8], [7, 6],[5,4]])
    otherMatrix31 = Matrix([[9], [8], [7]])
    otherMatrix13 = Matrix([[9, 8, 7]])
    otherMatrix33 = Matrix([[9, 8, 7], [6, 5, 4], [3, 2, 1]])

    print("1 = Посчитать")
    mm23_32 = matrix23 * otherMatrix32
    print(mm23_32)
    mm23_33 = matrix23 * otherMatrix33
    print(mm23_33)
    mm31_13 = matrix31 * otherMatrix13
    print(mm31_13)
    mm33_33 = matrix33 * otherMatrix33
    print(mm33_33)

    print("2 = Длина строки первой матрицы должна быть равна длине столбца второй матрицы\nnone")
    mn1 = matrix23 * otherMatrix13
    print(mn1)
    mn2 = matrix31 * otherMatrix31
    print(mn2)
    mn3 = matrix13 * otherMatrix13
    print(mn3)

#MultiplyCheck()

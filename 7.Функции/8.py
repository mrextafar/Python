# def nums(*args):
#     maxI = 0
#     args[0].sort()
#     tempList = []
#     for i in args[0]:
#         average = sum(args[0])/len(args[0])
#         if args[0].count(i)

import numpy as np

# Матрица смежности
M = np.array([[0, 1, 1, 0, 1, 0],
              [1, 0, 0, 1, 1, 0],
              [1, 0, 0, 0, 1, 1],
              [0, 1, 0, 0, 0, 1],
              [1, 1, 1, 0, 0, 1],
              [0, 0, 1, 1, 1, 0]])

# Начальное количество микробов в каждой вершине
initial_microbes = np.array([1, 1, 1, 1, 1, 1])

# Количество шагов
steps = 16

# Проведем шаги
for _ in range(steps):
    initial_microbes = M @ np.diag(initial_microbes) @ M.T

# Выведем количество микробов в первой вершине
result = round(initial_microbes[0])
print(result)
print("Вас приветсвует программа которая определяет победителя в ходе конкурса из 3-х человек при помощи их баллов в 3-х турах")
print("Введите количество баллов у первого участника в 1-ом, 2-ом, 3-ем туре соответственно используя клавишу ввода как разделитель")
m1 = int(input())
n1 = int(input())
p1 = int(input())
print("Введите количество баллов у второго участника в 1-ом, 2-ом, 3-ем туре соответственно используя клавишу ввода как разделитель")
m2 = int(input())
n2 = int(input())
p2 = int(input())
print("Введите количество баллов у третьего участника в 1-ом, 2-ом, 3-ем туре соответственно используя клавишу ввода как разделитель")
m3 = int(input())
n3 = int(input())
p3 = int(input())



#пока хз

class Uchastnik:
    def __init__(self, name, a, b, c, score):
        self.name = name
        self.a = a
        self.b = b
        self.c = c
        self.score = score



print("Введите кол-во баллов участника Иванова")
a1 = int(input())
b1 = int(input())
c1 = int(input())
score1 = a1+b1+c1
print("Введите кол-во баллов участника Петрова")
a2 = int(input())
b2 = int(input())
c2 = int(input())
score2 = a2+b2+c2
print("Введите кол-во баллов участника Сидорова")
a3 = int(input())
b3 = int(input())
c3 = int(input())
score3 = a3+b3+c3

firstTour = [a1,a2,a3]
firstTour.sort()

secondTour = [b1,b2,b3]
secondTour.sort()

thirdTour = [c1,c2,c3]
thirdTour.sort()

score = [score1, score2, score3]
score.sort()

p1 = Uchastnik("Ivanov", firstTour.index(a1), secondTour.index(b1), thirdTour.index(c1), score1)
p2 = Uchastnik("Petrov", firstTour.index(a2), secondTour.index(b2), thirdTour.index(c2), score2)
p3 = Uchastnik("Sidorov", firstTour.index(a3), secondTour.index(b3), thirdTour.index(c3), score3)

print(p1.name,p1.a,p1.b,p1.c,p1.score)
"""
place = [p1.a, p2.a, p3.a]
place.sort()
print(place.index(2))
"""
#1
import math as m
a = int(input("Введите значение для а: "))
b = int(input("Введите значение для b: "))
c = int(input("Введите значение для c: "))
D = (m.pow(b, 2)) - (4 * a * c)
if D > 0:
    print("ошибка")
    x1 = (-b + m.sqrt(D)) / (2*a)
    x2 = (-b - m.sqrt(D)) / (2*a)
    print("x1 = ", x1)
    print("x2 = ", x2)
elif D == 0:
    x = -b / 2*a
    print("x = ", x)
else:
    print("корней нет")

#2
import math as m
AB = int(input("Введите значение первого катета: "))
AC = int(input("Введите значение второго катета: "))
s = (AB*AC) / 2
print("Площадь: ", s)
BC = ((AC**2 + AC**2)**2)
print("Сторона BC: ", BC)
p = AB + AC + BC
print("Периметр: ", p)

#3
r = int(input("Введите радиус: "))
s = float (m.pi) * r**2
print(s)

#4
a = int(input("Введите сторону а: "))
b = int(input("Введите сторону b: "))
c = int(input("Введите сторону c: "))
if c < a + b:
    print("Треугольник существует")
else:
    print("Треугольник не существует")
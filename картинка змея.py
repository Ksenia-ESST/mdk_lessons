#1
import numpy as np
a = np.array([1, 2, 3, 4, 5])
print(a)
for i in a:
    print(i)
print(type(a))
print("второе состояние:", a*3)
print("общая сумма:", sum(a))
print("общая длинна:",len(a))
print("общая сумма *3:", sum(a)*3)
print("общая длинна *3:", len(a))

#2
a = int(input("Введите первое число: "))
b = int(input("Введите конечное число массива: "))
massiv = []
for i in range(a,b):
    vnesenie = (i)
    massiv.append(vnesenie)
print(massiv)

#3
i = np.matrix('1, 2, 8; 3, 4, 6; 5, 3, 1')
np.matrix([[1, 2, 8], [3, 4 ,6], [5, 3, 1]])
print(f'Матрица: \n{i}')
spisok = []
for row in i:
    spisok.append(row[0])
print("\nList: ", spisok)
print(i[1:3])
print(len(i))

#4
a = np.random.randint(1, 9, size=(2, 3))
print("Massiv First : ")
print(a)
b = np.random.randint(1, 9, size=(3, 2))
print("Massiv second : ")
print(b)
i = np.dot(a, b)
print("Произведения a and b: ", i)

#5
from PIL import Image
img = np.array(Image.open('pelmeshek.jpg'))
img_R = img.copy()
img_R[:, :, (1, 2)] = 0
img_B = img.copy()
img_B[:, :, (0, 1)] = 0
img_1 = Image.fromarray(img_R)
img_3 = Image.fromarray(img_B)
result = Image.new("RGB", (img.shape[1]*2, img.shape[0]*3))
result.paste(img_1, (img.shape[-1],img.shape[0]))
result.paste(img_3, (img.shape[1],img.shape[0]))
result.save("result.png", format="PNG")
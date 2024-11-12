import math as m
def addition_first(e=0.000001) -> float:
    n = 1
    summation = 0
    while True:
        inscrement = 1 / n
        summation = summation + inscrement
        n = n + 1
        if m.fabs(inscrement) < e:
            break
    print(f'n = {n}')
    return summation
def addition_second(e=0.000001) -> float:
    n = 1
    summation = 0
    while True:
        inscrement = n / m.pow(n, 2)
        summation = summation + inscrement
        n = n + 1
        if m.fabs(inscrement) < e:
            break
    print(f'n = {n}')
    return summation
def addition_third(e=0.000001) -> float:
    n = 2
    summation = 0
    while True:
        inscrement = m.log10(n) / n
        summation = summation + inscrement
        n = n + 1
        if m.fabs(inscrement) < e:
            break
    print(f'n = {n}')
    return summation
def addition_fourth(e=0.000001) -> float:
    n = 2
    summation = 0
    while True:
        inscrement = m.sin(n) / m.log10(n)
        summation = summation + inscrement
        n = n + 1
        if m.fabs(inscrement) < e:
            break
    print(f'n = {n}')
    return summation
def multiplication_first(e=0.000001) -> float:
    n = 2
    multiplication = 0 
    while True:
        inscrement = 1 / n * m.log10(n)
        multiplication = multiplication * (1 + inscrement)
        n = n + 1
        if m.fabs(inscrement) < e:
            break
    print(f'n = {n}')
    return multiplication
def multiplication_second(e=0.000001) -> float:
    n = 2
    multiplication = 0 
    while True:
        inscrement = n / (n - 1) * (n + 2)
        multiplication = multiplication * (1 + inscrement)
        n = n + 1
        if m.fabs(inscrement) < e:
            break
    print(f'n = {n}')
    return multiplication
def multiplication_third(e=0.000001) -> float:
    n = 1
    multiplication = 0 
    while True:
        inscrement = m.cos(n) / m.sin(m.pow(n, 2))
        multiplication = multiplication * (1 + inscrement)
        n = n + 1
        if m.fabs(inscrement) < e:
            break
    print(f'n = {n}')
    return multiplication
def multiplication_fourth(e=0.000001) -> float:
    n = 1
    multiplication = 0 
    while True:
        inscrement = m.atan(n) / (m.exp(n) - m.pi)
        multiplication = multiplication * (1 + inscrement)
        n = n + 1
        if m.fabs(inscrement) < e:
            break
    print(f'n = {n}')
    return multiplication
while True:
    print('Напишите "q" чтобы выйти')
    list = input("Выберите уравнение (1-8): ")
    list2 = int(input("Значение: "))
    if list == '1':
        print(addition_first(list2))
    elif list == '2':
        print(addition_second(list2))
    elif list == '3':
        print(addition_third(list2))
    elif list == '4':
        print(addition_fourth(list2))
    elif list == '5':
        print(multiplication_first(list2))
    elif list == '6':
        print(multiplication_second(list2))
    elif list == '7':
        print(multiplication_third(list2))
    elif list == '8':
        print(multiplication_fourth(list2))
    else:
        break
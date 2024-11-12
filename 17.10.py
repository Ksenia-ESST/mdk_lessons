import math as m
def addition_second1(n: int) -> float:
    summation = 0
    for i in range(n + 1):
        summation = summation + (m.fabs(m.pow(2, i) * m.log(i + 1) * m.log(i+2, 3)) ) **2
    return summation
def addition_second2(n: int) -> float:
    summation = 0
    for i in range(n + 1):
        summation = summation + (m.log(i) + m.factorial(i) * m.log(i+1, 5)**2 * m.log2(i))
    return summation 
def addition_second3(n: int) -> float:
    summation = 0
    for i in range(1, n + 1):
        summation = summation + m.pow(m.log(i, 2) * m.pow(3, i - 1) + i * m.log(2), 1/3)
    return summation
def addition_second4(n: int) -> float:
    summation = 0
    for i in range(n + 1):
        summation = summation + m.log(i+1) / (m.log(i+2, 10) * m.log(i+3, 7))
    return summation
def addition_second5(n: int) -> float:
    summation = 0
    for i in range(1, n + 1):
        summation = summation + (m.exp(i) + m.log(i) * m.log(i+2, 5)) **2
    return summation
def multiplication_first1(n: int) -> float:
    multiplication = 1
    for i in range(1, n + 1):
        multiplication = multiplication * (m.pow(2, -i) * m.log(i+1) + m.pow(1.2, i/12) * m.log(i+2))
    return multiplication
def multiplication_first2(n: int) -> float:
    multiplication = 1
    for i in range(1, n + 1):
        multiplication = multiplication * (3 * m.log(i+2, 2) - m.pow(e, -i) / m.log(i+1, 10) + m.pow(2, 1-2 * i))
    return multiplication
def multiplication_first3(n: int) -> float:
    multiplication = 1
    for i in range(1, n + 1):
        multiplication = multiplication * (m.sqrt(m.fabs(m.pow(5, i+1) / i**3 + m.log(i*2) - m.factorial(i))))
        return multiplication
def multiplication_first4(n: int) -> float:
    multiplication = 1
    for i in range(1, n + 1):
        summation = 0
        for k in range(1, i + 2):
            summation = summation + 1 / k
        multiplication = multiplication * (m.log(i+1) * m.exp(i/7) * summation)
    return multiplication
def multiplication_first5(n: int) -> float:
    multiplication = 1
    for i in range(1, n + 1):
        summation = 0
        for k in range(1, n + 3):
            summation = summation + m.log(k+1) * m.log2(i+2)
        multiplication = multiplication * summation
    return multiplication
while True:
    print('Напишите "q" чтобы выйти')
    choise = input("Выберите уравнение (1-10): ")
    choise2 = int(input("Значение: "))
    if choise == '1':
        print(addition_second1(choise2))
    elif choise == '2':
        print(addition_second2(choise2))
    elif choise == '3':
        print(addition_second3(choise2))
    elif choise == '4':
        print(addition_second4(choise2))
    elif choise == '5':
        print(addition_second5(choise2))
    elif choise == '6':
        print(multiplication_first1(choise2))
    elif choise == '7':
        print(multiplication_first2(choise2))
    elif choise == '8':
        print(multiplication_first3(choise2))
    elif choise == '9':
        print(multiplication_first4(choise2))
    elif choise == '10':
        print(multiplication_first5(choise2))
    else:
        break
    

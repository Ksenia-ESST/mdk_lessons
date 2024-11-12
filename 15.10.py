import math as m
def logarithm_first(x: float) -> float:
    return m.log(x+3) + m.exp(x-2) - m.log10(m.exp(x-3)) / 2*x-1
def logarithm_second(x: float) -> float:
     return m.fabs(m.log(m.factorial(int(x)))) + m.sqrt(m.log(x+2, 2)) - 1 / m.sqrt(m.log(x))
def logarithm_third(x:float) -> float:
    return m.log10(x**2 + 1) * (1 / m.exp(x-1)) - (1 / x**m.log(x+2))
def logarithm_fourth(x:float) -> float:
    return m.log((x+1),5) / m.sqrt(m.exp(x-2)) - m.log10(3*x / 2*m.pow(x, 3) - 1)
def trigonometry_first(x:float) -> float:
    return (m.sin(x)**3 * m.cos(2*x)) / m.fabs(m.tan(x/2)**2) + (1/m.tan(3*x))**2
def trigonometry_second(x:float) -> float:
    return m.sqrt(m.fabs(m.sin(3*x)**2 + m.cos(x)**2) / m.cos(2*x) - 1) * m.exp(m.sin(2*x+1) * 1/m.tan(x-1))
def trigonometry_third(x:float) -> float:
    return (m.asin(x)**2 + m.exp(m.acos(x)-1)) / m.sqrt(m.fabs(1/m.atan(x/2))) * m.pi * m.asin(m.fabs(x)) / x - m.pi
def trigonometry_fourth(x:float) ->float:
    return (m.exp(m.fabs(m.pi/2 - m.atan(x))) -m.pi) /m.sqrt(m.acos(x)**2 + 1) - m.exp(x**2) /(m.pi + 3 * m.atan(x)**2)
def choose():
    while True:
        i = int(input("Выберите пример 1-8: "))
        if i == 1:
            X=float(input("введи x:"))
            a = logarithm_first(X)
            print(a)
        elif i == 2:
            X=float(input("введи x:"))
            a = logarithm_second(X)
            print(a)
        elif i == 3:
            X=float(input("введи x:"))
            a = logarithm_third(X)
            print(a)
        elif i == 4:
            X=float(input("введи x:"))
            a = logarithm_fourth(X)
            print(a)
        elif i == 5:
            X=float(input("введи x:"))
            a = trigonometry_first(X)
            print(a)
        elif i == 6:
            X=float(input("введи x:"))
            a = trigonometry_second(X)
            print(a)
        elif i == 7:
            X=float(input("введи x:"))
            a = trigonometry_third(X)
            print(a)
        elif i == 8:
            X=float(input("введи x:"))
            a = trigonometry_fourth(X)
            print(a)
choose()
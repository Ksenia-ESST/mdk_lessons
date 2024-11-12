#1
def is_even(num):
    """
    This  function checks if the number is even or not even.
    """
    return "Четное" if num % 2 == 0 else "Нечетное"
print(is_even(2))
print(is_even(5))
print(is_even.__doc__)
#2
def age_category(age):
    """
    This function defines the age category.
    """
    return "Детский" if age < 14 else "Подростковый" if age < 18 else "Взрослый"
print(age_category(9))
print(age_category(16))
print(age_category(22))
print(age_category.__doc__)
#3
def check_sign(number):
    """
    This function checks whether the number is positive, negative or zero.
    """
    return "Положительное" if number > 0 else "Отрицательное" if number < 0 else "Ноль"
print(check_sign(-4))
print(check_sign(5))
print(check_sign(0))
print(check_sign.__doc__)
#4
def grade_evaluation(mark):
    """
    This function defines the student's grade category.
    """
    return "Ужасно" if mark  < 25 else "Нужно учиться" if mark < 50 else "Хорошо" if mark < 75 else "Отлично"
print(grade_evaluation(12))
print(grade_evaluation(32))
print(grade_evaluation(65))
print(grade_evaluation(99))
print(grade_evaluation.__doc__)
#5
def greeting(time):
    """
    This function defines the time of day category.
    """
    return "Доброе утро" if time < 12 else "Добрый день" if time < 17 else "Добрый вечер" if time < 22 else "Доброй ночи" 
print(greeting(10))
print(greeting(14))
print(greeting(19))
print(greeting(23))
print(greeting.__doc__)
#6
def average_grade(grades):
    """
    This function calculates the arithmetic mean of the estimates.
    """
    total_sum = sum(grades)
    avg = total_sum / len(grades)
    if avg <= 3:
        return "низкий"
    elif 3 < avg < 4:
        return "средний"
    else:
        return "высокий"
grades = [33, 54, 78, 99]
result = average_grade(grades)
print(f'результат: {result}')
print(average_grade.__doc__)
#7
def classify_number(num: int):
    """
    the classify_number() function, which takes a number and returns "Positive even", "Positive Odd", "Negative even", "Negative odd" or "Zero"
    """
    if num > 0 and num %2 == 0:
        return "Положительное и четное"
    elif num > 0 and num %2 != 0:
        return "Положительное и нечетное"
    elif num < 0 and num%2 == 0:
        return "Отрицательое и нечетное"
    elif num < 0 and num%2 != 0:
        return "Отрицательное и нечетное"
    else:
        return "zero"
print(classify_number(50))
print(classify_number(27))
print(classify_number(-6))
print(classify_number(-75))
print(classify_number(0))
print(classify_number.__doc__)
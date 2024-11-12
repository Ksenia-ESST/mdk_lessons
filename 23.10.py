#1
gen_class = (i**3 for i in range(1, 6))
print(type(gen_class))
print(next(gen_class))
print(next(gen_class))
print(next(gen_class))
print(next(gen_class))
print(next(gen_class))

#2
a, b, c = 0, 1, 0
fib_sequence = [ [a:= b, b:= c, c:= a + b][1] for _ in range(10)]
print(fib_sequence)

#3
def get_even(list_of_nums):
    for i in list_of_nums:
        if i % 2 == 0:
            yield i
list_of_nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print("Список: " + str(list_of_nums))
print("Только четные числа: ", end = " ")
for i in get_even(list_of_nums):
    print(i, end = " ")

#4
fruits = ['mango', 'banana', 'orange']
def letter(fruits):
    for fruit in fruits:
        yield fruit[0]
def fruits_length(fruits):
    for fruit in fruits:
        yield len(fruit)
def filtered_fruits(fruits):
    for fruit in fruits:
        if len(fruit) < 3:
            yield fruit
letters = list(letter(fruits))
fruits_length = list(fruits_length(fruits))
filtered_fruits = list(filtered_fruits(fruits))
print(letters)
print(fruits_length)
print(filtered_fruits)

#5
people = {'Valera': 23, 'Semen': 17, 'Egor': 21, 'Arseniy': 25}
list = {name: age for name, age in people.items() if age > 18}
print(list)

#6
list_meters = [2, 4, 6, 1, 3]
list_centimeters = {list * 100 for list in list_meters}
print(list_centimeters)

#7
import random 
import string
domains = ["example.com", "test.com", "myemail.com", "sample.net", "demo.org"]
def user_name(length):
    symbols = string.ascii_lowercase + string.digits
    letters = ''.join(random.choice(symbols) for _ in range(length))
    return letters
def email(num):
    email_list = []
    for _ in range(num):
        username = user_name(5)
        domain = random.choice(domains)
        emails = f"{username}@{domain}"
        email_list.append(emails)
    return email_list
num_emails = 10
random_email = email(num_emails)
print(random_email)
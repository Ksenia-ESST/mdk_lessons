#17.1
sandwich_orders = ['тунцовый', 'куриный', 'вегетарианский', 'бланк', 'с сырами']
finished_sandwiches = []
for sandwich in sandwich_orders:
    print(f"I made your {sandwich} sandwich.")
    finished_sandwiches.append(sandwich)
print("\nВсе изготовленные сэндвичи:")
for finished_sandwich in finished_sandwiches:
    print(f"- {finished_sandwich}")
#17.2
sandwich_orders = [
    'tuna sandwich with cheese',
    'chicken sandwich',
    'vegetable sandwich with cheese',
    'ham sandwich',
    'turkey sandwich',
    'beef sandwich with cheese',
    'club sandwich'
]
cheese_count = sum('with cheese' in order for order in sandwich_orders)
if cheese_count < 3:
    print("С сыром больше нет.")
while 'with cheese' in sandwich_orders:
    sandwich_orders.remove('with cheese')
finished_sandwiches = sandwich_orders.copy()
if 'with cheese' not in finished_sandwiches:
    print("В списке завершенных сэндвичей 'with cheese' нет.")
print("Заказы сэндвичей:", sandwich_orders)
print("Завершенные сэндвичи:", finished_sandwiches)
#17.3
def main():
    print("Здравствуйте! Где бы вы хотели провести отпуск.")
    destinations = []
    num_participants = int(input("Введите количество участников опроса: "))
    for i in range(num_participants):
        destination = input(f"Участник {i + 1}, введите место, где вы хотели бы провести отпуск: ")
        destinations.append(destination)
    results = {}
    for place in destinations:
        if place in results:
            results[place] += 1
        else:
            results[place] = 1
    print("\nРезультаты опроса:")
    for place, count in results.items():
        print(f"{place}: {count} голос(ов)")
if __name__ == "__main__":
    main()
#18.1 (16.09.24)
def favorite_book(title):
    print(f"One of my favorite books is {title}")
favorite_book("Alice in Wonderland")
#18.2
def make_shirt(size, text):
    print(f"Футболка размера {size} с надписью '{text}'")
make_shirt("M", "Fart!")
make_shirt(size="S", text="Nike")
#18.3
def make_shirt(size='L', text='I love Python'):
    print(f"Футболка размера {size} с текстом: {text}")
make_shirt()
make_shirt(size='S', text='Hello, Kay!')
#18.4
def describe_city(city, country='Country'):
    print(f"{city} is in {country}")
describe_city("Reykjavik", "Iceland")
describe_city("Omsk", "Russia")
describe_city("Tokyo", "Japan")
#18.5
def select_car():
    car = input("Какую машину вы бы хотели взять напрокат? ")
    print(f"Думаю, я смогу найти для вас {car}")
select_car()

#19.1 (17.09.24)
def city_country(city, country):
    return f"{city}, {country}"
print(city_country("Santiago", "Chile"))
print(city_country("Tokyo", "Japan"))
print(city_country("Moscow", "Russia"))
#19.2
def make_album(artist, album):
    return {'исполнитель': artist, 'альбом': album}
album1 = make_album('Macan', 'I AM')
album2 = make_album('Ранетки', 'Ранеткид')
album3 = make_album('Jubilee', 'DNA')
print(album1)
print(album2)
print(album3)
#19.3
def make_album(artist, album_title, tracks=None):
    album = {
        'artist': artist,
        'album_title': album_title,
    }
    if tracks is not None:
        album['tracks'] = tracks
    return album
album1 = make_album('Macan', 'I AM')
album2 = make_album('Jubilee', 'DNA', tracks=1)
print(album1)
print(album2)
#19.4
def make_album(artist_name, album_title):
    album = {
        'artist': artist_name,
        'title': album_title
    }
    return album
while True:
    print("\\nВведите информацию об альбоме (или 'выход' для завершения):")
    artist_name = input("Исполнитель: ")
    if artist_name.lower() == 'выход':
        break
    album_title = input("Название альбома: ")
    if album_title.lower() == 'выход':
        break
    album_info = make_album(artist_name, album_title)
    print("Созданный словарь альбома:", album_info)
print("Вы вышли из программы.")
#19.5
def show_messages(messages):
    for message in messages:
        print(message)
messages_list = [
    "Привет! Как дела?",
    "Сегодня отличный день!",
    "Как прошел твой уикенд?"
]
show_messages(messages_list)
#19.6
messages = ["Привет!", "Как дела?", "Не забудь о встрече.", "Увидимся позже."]
sent_messages = []
def send_messages(messages):
    while messages:
        current_message = messages.pop(0)
        print(f"Отправлено сообщение: {current_message}")
        sent_messages.append(current_message)
send_messages(messages)
print("\nОстались сообщения:", messages)
print("Отправленные сообщения:", sent_messages)
#19.7
def send_messages(messages):
    while messages:
        current_message = messages.pop()
        print(f"Отправлено сообщение: {current_message}")
messages = ["Привет!", "Как дела?", "Успехов в учебе!"]
messages_copy = messages[:]
send_messages(messages_copy)
print("Исходный список сообщений:", messages)
print("Список сообщений после отправки:", messages_copy)
#20.1 (17.09.24)
def show_messages(messages):
    for message in messages:
        print(message)
messages = [
    "Привет, как дела?",
    "Сегодня отличная погода.",
    "Хорошего дня!"
]
show_messages(messages)
#20.2
messages = ["Привет, как дела?", "Сегодня отличная погода.", "Хорошего дня!"]
sent_messages = []
def send_messages(messages):
    while messages:
        current_message = messages.pop(0)
        print(f"Отправка сообщения: {current_message}")
        sent_messages.append(current_message)
send_messages(messages)
print("\nОставшиеся сообщения:", messages)
print("Отправленные сообщения:", sent_messages)
#20.3
def send_messages(messages):
  """Выводит каждое сообщение из списка, имитируя отправку."""
  print("Отправляю следующие сообщения:")
  while messages:
    current_message = messages.pop()
    print(current_message)
messages = ["Привет!", "Как дела?", "Всё хорошо?", "Пока!"]
sent_messages = messages[:]
send_messages(sent_messages)
print("\nИсходный список:")
print(messages)
print("\nСписок отправленных сообщений:")
print(sent_messages)
#21.1(19.09.24)
def describe_sandwich(*ingredients):
    if ingredients:
        print("Вы заказали сэндвич с следующими компонентами:")
        for ingredient in ingredients:
            print(f"- {ingredient}")
    else:
        print("Вы не заказали сэндвич.")
describe_sandwich("помидоры", "огурцы", "сыр")
print()  
describe_sandwich("курица", "авокадо")
print() 
describe_sandwich("тунца", "майонез", "салат", "лук", "перец", "оливки")
#21.2
def build_profile(first, last, **user_info):
    profile = {}
    profile['first_name'] = first
    profile['last_name'] = last
    for key, value in user_info.items():
        profile[key] = value
    return profile
my_profile = build_profile('Филипп', 'Денин', age=19, city='PITER', hobby='танцы')
print(my_profile)
#21.3
def make_car(manufacturer, model, **kwargs):
    car_info = {
        'manufacturer': manufacturer,
        'model': model
    }
    for key, value in kwargs.items():
        car_info[key] = value
    return car_info
car = make_car('porshe', 'outback', color='black', tow_package=True)
print(car)
#8.5.1 return (19.09.24)
def сложение(a, b):
    """Функция для сложения двух чисел."""
    return a + b
if __name__ == "__main__":
    num1 = float(input("Введите первое число: "))
    num2 = float(input("Введите второе число: "))
    результат = сложение(num1, num2)
    print(f"Сумма {num1} и {num2} равна {результат}.")
#8.5.2
def get_even_numbers(input_list):
    even_numbers = [num for num in input_list if num % 2 == 0]
    return even_numbers
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = get_even_numbers(numbers)
print(even_numbers)
#8.5.3
values = [10, 20, 30, 40, 50]
total_sum = sum(values)
count = len(values)
mean = total_sum / count
print("Среднее значение выборки:", mean)
#8.5.4
string = "Лемур"
index_to_skip = 2  
for i in range(len(string)):
    if i == index_to_skip:
        pass
    else:
        print(string[i], end='')
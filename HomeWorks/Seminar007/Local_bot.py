from random import *
import json
import os
def clear(): return os.system('cls')


clear()

films = []


def save():
    with open('films.json', 'w', encoding='utf-8') as data:
        data.write(json.dumps(films, ensure_ascii=False))
    print('Наша фильмотека успешно сохранена в файле films.json!')


def load():
    with open('films.json', 'r', encoding='utf-8') as data:
        films = json.load(data)
    print('Фильмотека успешно загруженна!')


try:
   with open('films.json', 'r', encoding='utf-8') as data:
        films = json.load(data)
        print('Фильмотека успешно загруженна!')
except:
    films = []
    films.append('Интерстеллар')
    films.append('Хроники ридика')
    films.append('Крестный отец')
    films.append('Области тьмы')
    films.append('Пираты корибского моря')


print('Добро пожаловать в фильмотеку!)')

while True:
    command = input('\nВведите команду: ')

    if command == "/start":
        print('\nДобро пожаловать в бот - фильмотеку!!')
    elif command == '/all':
        print('\nВзгляните на текущий список фильмов:')
        print(films)
    elif command == '/add':
        f = input('\nВведите название фильма: ')
        films.append(f)
        print(f'\nФильм "{f}" успешно добавлен в коллекцию!')
    elif command == '/delite':
        f = input('\nВведите название фильма, который нужно удалить: ')
        if f in films:
            films.remove(f)
            print(f'\n Фильм "{films}" успешно удален!')
        else:
            print('\nТакого фильма нет в коллекции!')
    elif command == '/help':
        print('\n/all - Показать всю коллекцию фильмов.\n/add - Добавить название фильма в коллекцию.\
              \n/delite - Удалить название фильма из коллекции.\n/save - Сохранить коллекцию фильмов\
              \n/load - Загрузить коллекцию фильмов.\n/random - Выбрать случайный фильм из коллекции фильмов.')
    elif command == '/save':
        save()
        print('\nКоллекция фильмов успешно сохранена!')
    elif command == '/load':
        load()
        print('\nКоллекция фильмов успешно загруженна!')
    elif command == '/random':
        rnd = randint(0, len(films) - 1)
        print(f'\nЖребий выпал на - ' + choice(films))
    else:
        if command == '/stop':
            save()
            print(
                '\nБот завершил работу! Возвращайтесь к нам снова, будем рады нашей встрече!)')
            break
        else:
            print('\nНеопознаная команда, повторите попытку.\
                   \nВсе команды можно просмотреть введя /help или введите команду /stop, что бы завершить работу!')

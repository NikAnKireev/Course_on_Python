# Модуль функций

import os
import json


def clear(): return os.system('cls')  # Чистка консоли


def print_dic(arr):
    if arr != {}:
        print('----------------------------------')
        for key, value in arr.items():
            print(key, ': \nтел -', " \nпочта - " ' '.join(str(*x) for x in value))
            print('----------------------------------')
    else:
        print('\nВ справочнике еще нет контактов.')


def add_User(arr):
    try:
        word = input("Введите ФИО: ")
        numbers = int(input("Введите телефон: "))
        mail = input("Введите почту: ")
        arr[word] = [numbers], [mail]
    except:
        print('\nВы ввели строки вместо цифр во вкладке телефон. Повторите попытку.')


def save(arr):  # Сохранение данных
    with open('Phones_Book.json', 'w', encoding='utf-8') as data:
        data.write(json.dumps(arr, ensure_ascii=False))
    print('\nДанные успешно сохранены!\n')


def load(arr):  # Загрузка данных
    with open('Phones_Book.json', 'r', encoding='utf-8') as data:
        arr = json.load(data)
    print('\nДанные успешно загруженны!\n')


def delite(arr):
    # del arr[input('Введите ключь: ')]
    arr.pop(input('Введите ключь: '), 'no')
# def search():
#     res = []
#     sear = input('Введите поисковой запрос: ')
#     for sear in directory:
#         isExsist

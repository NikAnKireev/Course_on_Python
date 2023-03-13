from function import *

clear()

print('Команды справочника:\
\n1 - Показать все контакты\
\n2 - Добавить контакт\
\n0 - Завершить использованние программы')

direct = {}
with open('Phones_Book.json', 'r', encoding='utf-8') as data:
    direct = json.load(data)
print('\nДанные успешно загруженны!\n')

while True:
    command = input('Введите команду: ')

    if command == '1':
        print_dic(direct)
    elif command == '2':
        add_User(direct)
        save(direct)
    elif command == '0':
        save(direct)
        break

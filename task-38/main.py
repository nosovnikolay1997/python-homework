#!/bin/python
import sys

book_path = 'phonebook.txt'

def parse_file():
    result = list()
    with open(book_path, 'r') as book:
        lines = [l.rstrip('\n') for l in book.readlines()]
        result = list(zip(lines[0::4], lines[1::4], lines[2::4], lines[3::4]))
    return result

def print_entry(i):
    print(str(i + 1) + ".")
    print("Фамилия: " + entries[i][0])
    print("Имя: " + entries[i][1])
    print("Отчество: " + entries[i][2])
    print("Номер телефона: " + entries[i][3])
    print()

def print_book():
    print(entries)
    print(len(entries))
    for i in range(len(entries)):
        print_entry(i)

def search():
    query = input("Введите поисковый запрос: ").lower()
    for i in range(len(entries)):
        if query in ''.join(entries[i]).lower():
            print_entry(i)

input_entry = lambda : (input("Фамилия: "), input("Имя: "), input("Отчество: "), input("Номер телефона: "))

add = lambda : entries.append(input_entry())

def modify():
    i = int(input("Введите номер записи для изменения: ")) - 1
    if 0 <= i < len(entries):
        entries[i] = input_entry()
    else:
        print("Такой записи нет.")

def delete():
    i = int(input("Введите номер записи для удаления: ")) - 1
    if 0 <= i < len(entries):
        entries.pop(i)
    else:
        print("Такой записи нет.")

def save_and_exit():
    with open(book_path, 'w') as book:
        for last_name, first_name, middle_name, phone_number in entries:
            book.write(last_name + '\n' + first_name + '\n' + middle_name + '\n' + phone_number + '\n')
    sys.exit()

options = {
1 : ("Показать весь справочник", print_book),
2 : ("Поиск", search),
3 : ("Добавить запись", add),
4 : ("Изменить запись", modify),
5 : ("Удалить запись", delete),
6 : ("Сохранить и выйти", save_and_exit),
7 : ("Выйти без сохранения", sys.exit)
}

entries = parse_file()

while True:
    for command_number, (command_name, __) in options.items():
        print(str(command_number) + ". " + command_name)
    command = int(input("Введите номер комманды: "))
    if command in options:
        options[command][1]()
    else:
        print("Такой комманды нет.")


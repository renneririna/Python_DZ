# функции для работы с пользователем

def select_op():
    op = int(input("Выбери что хочешь сделать:\n1-Добавление пользователя\n2-Поиск\n3-Удаление\n4-Изменение\n5-Напечатать все записи\n6-Выход\n"))
    return op

def get_name():
    name = input("Введи имя: ")
    telephone = input("Введи телефон: ")
    string = name + "; " + telephone + "\n"
    return string

def print_info(*args):
    for res in args:
        if isinstance(res, list):
            counter = 1
            for string in res:
                print(f"{counter}) {string.strip()}")
                counter += 1
        if isinstance(res, str):
            print(res)

def get_some_info():
    char = input("Введи символ для поиска: ").lower()
    return char

def select_name():
    num = int(input("Выбери нужную строчку: "))
    return num - 1
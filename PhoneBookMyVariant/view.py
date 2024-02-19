def select_op():
    op = int(input('Выберите действие:\n'
                    '1. Добавить контакт:\n'
                    '2. Поиск контакта:\n'
                    '3. Удалить контакт:\n'
                    '4. Изменить контакт:\n'
                    '5. Показать все контакты:\n'
                    '6. Выход\n'))
    return op

def get_name():
    name = input('Введите имя:\n')
    number = input('Введите номер телефона:\n')
    data = name + ';' + number + '\n'
    return data

def print_info(*args):
    for res in args:
        if isinstance(res, list):
            count = 1
            for data in res:
                print(f"{count}) {data.strip()}")
                count += 1
        if isinstance(res, str):
            print(res)


def get_info():
    char = input("Введи имя для поиска\n").lower()
    return char

def select_name():
    num = int(input("Выбери номер нужной строки:\n "))
    return num-1
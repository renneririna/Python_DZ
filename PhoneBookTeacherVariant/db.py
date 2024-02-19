# функции для работы с базой данных

def write_name(string):
    with open('data.txt', 'a', encoding="utf-8") as file:
        file.write(string)
    return "Имя добавлено"

def search_name(char):
    with open('data.txt', 'r', encoding="utf-8") as file:
        lst = file.readlines()
        name_accept = []
        for line in lst:
            if char in line.lower():
                name_accept.append(line)
        return lst, name_accept, "Поиск завершен!"

def change_name(old_lst, delete_line, new_line = None):
    with open('data.txt', 'w', encoding="utf-8") as file:
        for line in old_lst:
            if line == delete_line:
                if new_line:
                    file.write(new_line)
                continue
            file.write(line)
    return "Запись удалена!" if not new_line else "Запись изменена!"

def get_all():
     with open('data.txt', 'r', encoding="utf-8") as file:
         return file.read()
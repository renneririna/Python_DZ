def write_name(data):
    with open("text.txt", "a", encoding='utf-8') as file:
        file.write(data)
    return "Имя добавлено"

def search_info(char):
     with open('text.txt', 'r', encoding='utf-8') as file:
        lst = file.readlines()
        name_accept = []
        for line in lst:
            if char in line.lower():
                name_accept.append(line)
        return lst, name_accept, "Поиск завершен!"

def change_name(old_lst, delete_line, new_line = None):
    with open('text.txt', 'w', encoding='utf-8') as file:
        for line in old_lst:
            if line == delete_line:
                if new_line:
                    file.write(new_line)
                continue
            file.write(line)
    return "Запись изменена!" if new_line else "Запись удалена"


def book_view():
     with open('text.txt', 'r', encoding='utf-8') as file:
        return file.read()       
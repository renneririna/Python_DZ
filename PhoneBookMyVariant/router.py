from view import *
from database import *

def main():
    while True:
        ans = select_op()
        if ans == 1:
            name = get_name()
            result = write_name(name)
            print_info(result)
        elif ans == 2:
            char = get_info()
            full_lst, accept_lst, result = search_info(char)
            print(accept_lst, result)
        elif ans == 3:
            char = get_info()
            full_lst, accept_lst, result = search_info(char)
            print(accept_lst, result)
            selected_num = select_name()
            result = change_name(full_lst, accept_lst[selected_num])
            print_info(result)
        elif ans == 4:
            char = get_info()
            full_lst, accept_lst, result = search_info(char)
            print(accept_lst, result)
            selected_num = select_name()
            new_line = get_name()
            result = change_name(full_lst, accept_lst[selected_num], new_line)
            print_info(result)
        elif ans == 5:
            result = book_view()
            print_info(result)
        elif ans == 6:
            break
main()            

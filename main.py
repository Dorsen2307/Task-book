import os.path
from menu_header import *


# main
if __name__ == '__main__':
    if not os.path.isfile('task.db'):
        created_db()

        raise DBNotFoundError

    ex = True
    while ex:
        output_menu()

        input_number_menu = input_with_type_check('Enter the menu item: ', int)

        try:
            ex = check_input_user(input_number_menu)
        except InputValueError:
            print('\nThere is no such menu item')

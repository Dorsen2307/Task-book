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

        input_user = input('Enter the menu item: ')

        try:
            ex = validate_input_user(input_user)
        except InvalidInputError:
            print('\nInvalid Input')

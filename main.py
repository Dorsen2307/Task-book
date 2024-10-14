class InvalidInput(Exception):
    pass

def output_menu():
    print('''
    ---------- The task book ----------

    1. Check the tasks
    2. Add a task
    3. Delete a task

    ------------------------------''')

def validate_input_user(input_user):
    if input_user == '0':
        return False
    if input_user == '1':
        check_task()
        return True
    if input_user == '2':
        add_task()
        return True
    if input_user == '3':
        delete_task()
        return True
    raise InvalidInput

def check_task():
    pass

def add_task():
    pass

def delete_task():
    pass

# main
ex = True
while ex:
    output_menu()
    input_user = input('Enter the menu item: ')
    try:
        ex = validate_input_user(input_user)
    except InvalidInput:
        print('Invalid Input')

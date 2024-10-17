from datetime import datetime
from TaskProject.db import *
from Exceptions.Error import *

def output_menu():
    print('''
    ---------- The task book ----------
    1. Check the tasks
    2. Add a task
    3. Delete a task
    4. Update a task
    0. Exit
    ------------------------------''')

def get_and_output_records_tasks():
    tasks, columns = view_tasks()

    print('\n<<<<<<<<<< List of records >>>>>>>>>>')

    for task in range(0, len(tasks)):
        for column in range(0, len(columns)):
            print(f'{columns[column][0].capitalize()}: {tasks[task][column]}')

        print()

    print('<<<<<<<<<<>>>>>>>>>>')

def input_user_for_added_task():
    print('\n<<<<<<<<<< Added record >>>>>>>>>>')

    title = input_with_type_check('Title: ', str)
    description = input_with_type_check('Description: ', str)
    due_date = input_with_type_check('Due date (dd.mm.yyyy): ', 'date', '%d.%m.%Y')

    added_task(title, description, due_date)

def deleting_entry():
    print('\n<<<<<<<<<< Deleting records >>>>>>>>>>')

    get_and_output_records_tasks()

    id_task = input_with_type_check('Task ID: ', int)

    deleted_task(id_task)

def changed_record_tasks():
    print('\n<<<<<<<<<< Changing records >>>>>>>>>>')

    get_and_output_records_tasks()

    id_task = input_with_type_check('Enter the task id to change: ', int)
    title_update = input_with_type_check('Title: ', str)
    description_update = input_with_type_check('Description: ', str)
    due_date_update = input_with_type_check('Due date (dd.mm.yyyy): ', 'date', '%d.%m.%Y')
    status_update = input_with_type_check('Status: ', str)

    updated_date_update = datetime.now().strftime('%Y.%m.%d %H:%M:%S')

    changed_task(id_task, title_update, description_update, due_date_update, status_update, updated_date_update)

def check_input_user(user_input):
    if user_input == 0:
        return False
    if user_input == 1:
        get_and_output_records_tasks()
        return True
    if user_input == 2:
        input_user_for_added_task()
        return True
    if user_input == 3:
        deleting_entry()
        return True
    if user_input == 4:
        changed_record_tasks()
        return True

    raise InputValueError

def input_with_type_check(prompt, expected_type, date_format = None):
    """
    Запрашивает у пользователя ввод и проверяет его тип.

    :param prompt: Строка, которая будет показана пользователю.
    :param expected_type: Ожидаемый тип данных (int, float, str).
    :return: Введенное значение, преобразованное в ожидаемый тип.
    """
    while True:
        user_input = input(prompt)

        try:
            if expected_type == int:
                return int(user_input)
            elif expected_type == float:
                return float(user_input)
            elif expected_type == str:
                return user_input
            elif expected_type == 'date':
                if date_format is None:
                    print('The date format is not specified.')
                    return
                return datetime.strptime(user_input, date_format).date()
            else:
                raise ValueError("Unsupported data type.")
        except ValueError:
            if expected_type == 'date':
                print(f'Error: enter the date in the format {date_format}.')
            else:
                print(f'Error: enter the type value {expected_type.__name__}.')
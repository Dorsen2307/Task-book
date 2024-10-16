import sqlite3

def connected_db():
    connect_db = sqlite3.connect('task.db')
    cursor = connect_db.cursor()

    return connect_db, cursor

def close_db(connect, cursor):
    cursor.close()
    connect.close()

def created_db():
    '''Создает БД.'''
    connect, cursor = connected_db()

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Tasks (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT NOT NULL,
        description TEXT,
        due_date DATE,
        status TEXT NOT NULL DEFAULT 'New',
        created_date DATE NOT NULL DEFAULT CURRENT_DATETIME,
        updated_date DATE NOT NULL DEFAULT CURRENT_DATETIME)''')

    close_db(connect, cursor)

    print('\nDatabase created successfully.')

def view_tasks():
    '''Выводит все записи из БД. Возвращает список записей.'''
    connect, cursor = connected_db()

    cursor.execute('SELECT * FROM tasks')

    all_tasks = cursor.fetchall()
    column_names = cursor.description

    close_db(connect, cursor)

    return all_tasks, column_names

def added_task(title, description, due_date):
    '''Добавляет запись в БД.'''
    connect, cursor = connected_db()

    cursor.execute('INSERT INTO tasks(title, description, due_date) VALUES(?, ?, ?)', (title, description, due_date,))

    connect.commit() # фиксируем изменения в БД
    close_db(connect, cursor)

    print('\nThe entry was successfully added.')

def deleted_task(id):
    '''Удаляет запись из БД по id.'''
    connect, cursor = connected_db()

    cursor.execute('DELETE FROM tasks WHERE id=?', (id,))

    connect.commit()
    close_db(connect, cursor)

    print('\nThe record was successfully deleted.')

def changed_task(id, title, description, due_date, status, updated_date):
    '''Изменяет запись по id.'''
    connect, cursor = connected_db()

    updates = []
    params = []

    if title:
        updates.append('title = ?')
        params.append(title)
    if description:
        updates.append('description = ?')
        params.append(description)
    if due_date:
        updates.append('due_date = ?')
        params.append(due_date)
    if status:
        updates.append('status = ?')
        params.append(status)
    if updated_date:
        updates.append('updated_date = ?')
        params.append(updated_date)

    params.append(id)

    sql = f'UPDATE tasks SET {", ".join(updates)} WHERE id=?'

    cursor.execute(sql, params)

    connect.commit()
    close_db(connect, cursor)

    print('\nThe record was successfully updated.')
import sqlite3

def create_db():
    connect_db = sqlite3.connect('task.db')
    cursor = connect_db.cursor()
    cursor.execute('')
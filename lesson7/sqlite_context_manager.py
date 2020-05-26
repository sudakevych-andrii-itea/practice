# Написать контекстный менеджер для работы с SQLite DB

import sqlite3


class SQLite:
    def __init__(self, db_name):
        self.db_name = db_name

    def __enter__(self):
        self.conn = sqlite3.connect(self.db_name)
        return self.conn.cursor()

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.conn.commit()
        self.conn.close()


if __name__ == '__main__':
    with SQLite('example.db') as cur:
        cur.execute("CREATE TABLE readle(id INTEGER PRIMARY KEY AUTOINCREMENT)")

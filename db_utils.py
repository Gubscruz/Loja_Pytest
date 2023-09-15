import sqlite3 as sql
from funcoes import *



class Sql():

    def __init__(self):
        conn = sql.connect('./db/e_magic_shop_v2.db')
        cursor = conn.cursor()

        self.conn = conn
        self.cursor = cursor

    def insert(self, table_name, columns, values, data):
        self.cursor.executemany(f'INSERT INTO {table_name} ({columns}) VALUES ({values})', data)
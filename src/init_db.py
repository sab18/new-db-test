import sqlite3


def initialize_database(db_title,table_name,*args):
    conn = sqlite3.connect(db_title)
    cursor = conn.cursor()
    cursor.execute(f"CREATE TABLE {table_name} {args}")

    conn.commit()
    cursor.close()
    conn.close()

db_title='db_name.db'
table_name='test_table'


initialize_database(db_title,table_name, 'name','name2')
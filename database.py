#
# import sqlite3
#
# database = sqlite3.connect('database.db')
# cursor = database.cursor()
# # INSERT
# # INTO
# # users(id, language, name, phone, user_name, telegram_id, city)
# # VALUES(?, ?, ?, ?, ?, ?, ?)
#
# def create_users_table():
#     cursor.execute('''
#     CREATE TABLE IF NOT EXISTS users(
#         user_id INTEGER PRIMARY KEY AUTOINCREMENT,
#         language TEXT DEFAULT uz,
#         full_name TEXT,
#         phone TEXT,
#         user_name TEXT,
#         telegram_id BIGINT NOT NULL UNIQUE,
#         city TEXT DEFAULT Tashkent
#     )
#     ''')
#
#
# def delete():
#     cursor.execute('''
#      DROP TABLE IF EXISTS users''')
#
#
# create_users_table()
#
# database.commit()
# database.close()
# import sqlite3
#
#
# def create_users_table():
#     # Открываем соединение с базой данных
#     conn = sqlite3.connect('database.db')
#     cursor = conn.cursor()
#
#     # Создаем таблицу, если она не существует
#     cursor.execute('''
#         CREATE TABLE IF NOT EXISTS users (
#             id INTEGER PRIMARY KEY AUTOINCREMENT,
#             language TEXT DEFAULT 'uz',
#             name TEXT,
#             phone TEXT,
#             user_name TEXT,
#             telegram_id BIGINT NOT NULL UNIQUE,
#             city TEXT DEFAULT 'Tashkent'
#         )
#     ''')
#
#     # Сохраняем изменения и закрываем соединение
#     conn.commit()
#     conn.close()
#
#
# def delete_users_table():
#     # Открываем соединение с базой данных
#     conn = sqlite3.connect('database.db')
#     cursor = conn.cursor()
#
#     # Удаляем таблицу, если она существует
#     cursor.execute('DROP TABLE IF EXISTS users')
#
#     # Сохраняем изменения и закрываем соединение
#     conn.commit()
#     conn.close()
#
#
# # Создаем таблицу при запуске скрипта
# create_users_table()

import sqlite3

database = sqlite3.connect('database.db')
cursor = database.cursor()


def create_users_table():
    with sqlite3.connect('database.db') as db:
        cursor = db.cursor()
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS users(
            user_id INTEGER PRIMARY KEY AUTOINCREMENT,
            language TEXT DEFAULT 'uz',
            full_name TEXT,
            phone TEXT,
            user_name TEXT,
            telegram_id BIGINT NOT NULL UNIQUE, 
            city TEXT DEFAULT 'Tashkent'
        )
        ''')
        cursor.execute('''CREATE TABLE IF NOT EXISTS cases (
                                id INTEGER PRIMARY KEY AUTOINCREMENT,
                                user_id INTEGER,
                                name TEXT,
                                phone TEXT,
                                city TEXT,
                                scammer_name TEXT,
                                theft_amount TEXT,
                                fraud_method TEXT,
                                exchange_name TEXT,
                                scam_wallet_address TEXT,
                                case_id TEXT,
                                serial_number TEXT,
                                code_word TEXT
                            )''')
        db.commit()


def delete():
    cursor.execute('''
     DROP TABLE cases''')
delete()
create_users_table()
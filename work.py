# import sqlite3
#
#
# async def add_user(id, language, name, phone, user_name, telegram_id, city):
#     async with sqlite3.connect('database.db') as db:
#         await db.execute('''
#             INSERT INTO users (id, language, name, phone, user_name, telegram_id, city) VALUES (?, ?, ?, ?, ?, ?, ?)
#         ''', (id, language, name, phone, user_name, telegram_id, city))
#         await db.commit()
#
#
# async def get_user(user_id):
#     async with sqlite3.connect('database.db') as db:
#         async with db.execute('''
#             SELECT * FROM users WHERE id=?
#         ''', (user_id,)) as cursor:
#             return await cursor.fetchone()
#
# async def get_lang(user_id):
#     async with sqlite3.connect('database.db') as db:
#         async with db.execute('''
#             SELECT language FROM users WHERE id=?
#         ''', (user_id,)) as cursor:
#             return await cursor.fetchone()
import sqlite3


def add_user(lang, name, phone, user_name, telegram_id, city):
    with sqlite3.connect('database.db') as db:
        cursor = db.cursor()
        cursor.execute('''
            INSERT INTO users (language, full_name, phone, user_name, telegram_id, city) 
            VALUES (?, ?, ?, ?, ?, ?)
        ''', (lang, name, phone, user_name, telegram_id, city))
        db.commit()

def get_user(user_id):
    with sqlite3.connect('database.db') as db:
        cursor = db.cursor()
        cursor.execute('''
            SELECT * FROM users WHERE telegram_id=?
        ''', (user_id,))
        return cursor.fetchone()


def save_case(user_id, name, phone, city, scammer_name, theft_amount, fraud_method, exchange_name, scam_wallet_address, case_id, serial_number, code_word):
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()

    cursor.execute('''INSERT INTO cases (user_id, name, phone, city, scammer_name, theft_amount, fraud_method, exchange_name, scam_wallet_address, case_id, serial_number, code_word)
                      VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''',
                   (user_id, name, phone, city, scammer_name, theft_amount, fraud_method, exchange_name, scam_wallet_address, case_id, serial_number, code_word))

    conn.commit()
    conn.close()


def get_lang(user_id):
    with sqlite3.connect('database.db') as db:
        cursor = db.cursor()
        cursor.execute('''
            SELECT language FROM users WHERE telegram_id=?
        ''', (user_id,))
        return cursor.fetchone()


# def save_case(user_id, name, phone, city, scammer_name, theft_amount, fraud_method, exchange_name, scam_wallet_address, case_id):
#     conn = sqlite3.connect('database.db')
#     cursor = conn.cursor()
#
#     cursor.execute('''INSERT INTO cases (user_id, name, phone, city, scammer_name, theft_amount, fraud_method, exchange_name, scam_wallet_address, case_id)
#                       VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''',
#                    (user_id, name, phone, city, scammer_name, theft_amount, fraud_method, exchange_name, scam_wallet_address, case_id))
#
#     conn.commit()
#     conn.close()
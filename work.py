import sqlite3


#ef select_user_lang(chat_id):
#   database = sqlite3.connect('lawyer.db')
#   cursor = database.cursor()
#   cursor.execute('''SELECT language FROM users WHERE telegram_id =?''',
#                  (chat_id,))
#   lang = cursor.fetchone()[0]
#   database.commit()
#   database.close()
#   return lang


def set_user_phone(chat_id, phone_number):
    database = sqlite3.connect('lawyer.db')
    cursor = database.cursor()
    cursor.execute('''UPDATE users SET phone = ? WHERE telegram_id = ?''',
                   (phone_number, chat_id))
    database.commit()
    database.close()


def set_user_language(chat_id, language):
    database = sqlite3.connect('lawyer.db')
    cursor = database.cursor()
    cursor.execute('''UPDATE users SET language = ? WHERE telegram_id = ?''',
                   (language, chat_id))
    database.commit()
    database.close()


def first_select_user(chat_id):
    database = sqlite3.connect('lawyer.db')
    cursor = database.cursor()
    cursor.execute('''
    SELECT * FROM users WHERE telegram_id = ? 
    ''', (chat_id,))
    user = cursor.fetchone()
    database.close()
    return user


def select_user_lang(chat_id):
    database = sqlite3.connect('lawyer.db')
    cursor = database.cursor()
    cursor.execute('''SELECT language FROM users WHERE telegram_id =?''',
                   (chat_id,))
    lang = cursor.fetchone()[0]
    database.commit()
    database.close()
    return lang


def register_user(chat_id, full_name, phone):
    database = sqlite3.connect('lawyer.db')
    cursor = database.cursor()
    cursor.execute('''
    INSERT INTO users(chat_id, full_name, phone)
    VALUES (?,?,?)
        ''', (chat_id, full_name, phone))
    database.commit()
    database.close()


def create_carts(chat_id):
    database = sqlite3.connect('lawyer.db')
    cursor = database.cursor()
    cursor.execute('''
    INSERT INTO carts(users_id) VALUES (
    (
           SELECT user_id FROM users WHERE telegram_id = ?
           )
           )
           ''', (chat_id,))
    database.commit()
    database.close()


def get_products_by_path(path_id):
    database = sqlite3.connect('lawyer.db')
    cursor = database.cursor()
    cursor.execute('''
    SELECT product_id, product_name FROM products
    WHERE path_id = ?;
    ''', (path_id, ))
    products = cursor.fetchall()
    database.close()
    return products


def get_categories():
    database = sqlite3.connect('lawyer.db')
    cursor = database.cursor()
    cursor.execute('''
    SELECT * FROM categories;
    ''')
    categories = cursor.fetchall()
    database.close()
    return сategories


def create_carts(chat_id):
    database = sqlite3.connect('lawyer.db')
    cursor = database.cursor()
    cursor.execute('''
    INSERT INTO carts(user_id) VALUES (
    (
           SELECT user_id FROM users WHERE telegram_id = ?
           )
           )
           ''', (chat_id,))
    database.commit()
    database.close()


#def get_products_by_path(path_id):
#    database = sqlite3.connect('lawyer.db')
#    cursor = database.cursor()
#    cursor.execute('''
#    SELECT product_id, product_name FROM products
#    WHERE path_id = ?;
#    ''', (path_id, ))
#    products = cursor.fetchall()
#    database.close()
#    return products
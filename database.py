
import sqlite3

database = sqlite3.connect('lawyer.db')
cursor = database.cursor()


def create_users_table():
    database = sqlite3.connect('lawyer.db')
    cursor = database.cursor()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS users(
        user_id INTEGER PRIMARY KEY AUTOINCREMENT,
        full_name TEXT,
        language VARCHAR(2),
        telegram_id BIGINT NOT NULL UNIQUE,
        phone TEXT
    )
    ''')


def create_carts_table():
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS carts(
        cart_id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER REFERENCES users(user_id) UNIQUE,
        total_products INTEGER DEFAULT 0,
        total_price DECIMAL(12, 2) DEFAULT 0 
    )
    ''')


def create_categories_table():
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS categories(
    category_id INTEGER PRIMARY KEY AUTOINCREMENT,
    category_name VARCHAR(20) NOT NULL UNIQUE
    )
    ''')


def create_product_table():
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS products(
        product_id INTEGER PRIMARY KEY AUTOINCREMENT,
        category_id INTEGER NOT NULL,
        product_name TEXT,
        image TEXT,
        
        FOREIGN KEY(category_id) REFERENCES categories(category_id)
    )
    ''')


create_users_table()
create_carts_table()

database.commit()
database.close()

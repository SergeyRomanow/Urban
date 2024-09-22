# ============================================================================

# Coding            : utf-8

# Script Name	    : crud_functions.py
# File              : module_10_*.py

# Author			: Sergey Romanov
# Created			: 01.10.2024
# Last Modified	    : 01.10.2024
# Version			: 1.0.001

# Modifications	:
# Modifications	: 1.0.1 - Tidy up the comments and syntax

# Description       : main script
# Description		: This will go through
#                     and backup all my automator services workflows

# ============================================================================

from threading import Thread
from time import sleep
import sqlite3

__author__ = 'Sergey Romanov'
__version__ = '1.0.001'

RSL_DEBUG = True


#

# Создайте файл crud_functions.py и напишите там следующие функции:
# initiate_db, которая создаёт таблицу Products, если она ещё не создана при
# помощи SQL запроса.
# Эта таблица должна содержать следующие поля:
# id - целое число, первичный ключ
# title(название продукта) - текст (не пустой)
# description(описание) - тест
# price(цена) - целое число (не пустой)
def initiate_db ( ) :
    """

    """
    conn = sqlite3.connect ( 'products.db' )
    cursor = conn.cursor ( )
    cursor.execute (
            '''CREATE TABLE IF NOT EXISTS Products (
                              id INTEGER PRIMARY KEY AUTOINCREMENT,
                              title TEXT NOT NULL,
                              description TEXT,
                              price INTEGER NOT NULL)'''
            )
    conn.commit ( )
    conn.close ( )


# Создайте функцию get_all_products, которая возвращает все записи из
# таблицы Products,
# полученные при помощи SQL запроса.
def get_all_products ( ) :
    """

    @return:
    @rtype:
    """
    conn = sqlite3.connect ( 'products.db' )
    cursor = conn.cursor ( )
    cursor.execute ( "SELECT * FROM Products" )
    products = cursor.fetchall ( )
    conn.close ( )
    return products


# Перед запуском бота пополните вашу таблицу Products 4 или более записями
# для последующего вывода в чате Telegram-бота.
def add_products ( ) :
    """

    """
    conn = sqlite3.connect ( 'products.db' )
    cursor = conn.cursor ( )

    for i in range ( 1, 5 ) :
        cursor.execute (
                "SELECT * FROM Products WHERE title = ?", (f'Продукт {i}',)
                )
        product = cursor.fetchone ( )

        if product is None :
            cursor.execute (
                    "INSERT INTO Products (title, description, price) VALUES "
                    "(?, "
                    "?, ?)",
                    (f'Продукт {i}', f'Описание {i}', i * 100)
                    )

    conn.commit ( )
    conn.close ( )

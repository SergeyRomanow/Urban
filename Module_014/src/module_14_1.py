# ============================================================================

# Coding            : utf-8

# Script Name	    : Создание потоков
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


"""
2024/01/15 00:00|
Домашнее задание по теме
"Асинхронность на практике"

Цель:
приобрести навык использования асинхронного запуска функций на практике

Задача "Асинхронные силачи":

Необходимо сделать имитацию соревнований по поднятию шаров Атласа.

Напишите асинхронную функцию start_strongman(name, power),
где
name - имя силача,
power - его подъёмная мощность.

Реализуйте следующую логику в функции:

В начале работы должна выводиться строка - 'Силач <имя силача> начал
соревнования.'

После должна выводиться строка - 'Силач <имя силача> поднял <номер шара>' с
задержкой обратно пропорциональной его силе power.

Для каждого участника количество шаров одинаковое - 5.

В конце поднятия всех шаров должна выводится строка 'Силач <имя силача>
закончил соревнования.'

Также напишите асинхронную функцию start_tournament, в которой создаются 3
задачи для функций start_strongman.
Имена(name) и силу(power) для вызовов
функции start_strongman можете выбрать самостоятельно.

После поставьте каждую задачу в ожидание (await).

Запустите асинхронную функцию start_tournament методом run.

Пример результата выполнения программы:
Переданные аргументы в функции start_strongman:
'Pasha', 3
'Denis', 4
'Apollon', 5
Вывод на консоль:
Силач Pasha начал соревнования
Силач Denis начал соревнования
Силач Apollon начал соревнования
Силач Apollon поднял 1 шар
Силач Denis поднял 1 шар
Силач Pasha поднял 1 шар
Силач Apollon поднял 2 шар
Силач Denis поднял 2 шар
Силач Apollon поднял 3 шар
Силач Pasha поднял 2 шар
Силач Denis поднял 3 шар
Силач Apollon поднял 4 шар
Силач Pasha поднял 3 шар
Силач Apollon поднял 5 шар
Силач Apollon закончил соревнования
Силач Denis поднял 4 шар
Силач Denis поднял 5 шар
Силач Denis закончил соревнования
Силач Pasha поднял 4 шар
Силач Pasha поднял 5 шар
Силач Pasha закончил соревнования

Примечания:

Для обозначения асинхронной функции используйте оператор async.
Для постановки задачи в режим ожидания используйте оператор await.
Для задержки в асинхронной функции используйте функцию sleep из пакета asyncio.
Для запуска асинхронной функции используйте функцию run из пакета asyncio.
"""
from __future__ import absolute_import

# from .__init__ import main

__author__ = 'Sergey Romanov'
__version__ = '1.0.001'

RSL_DEBUG = True

# module_14_1.py

# Домашнее задание по теме "Создание БД, добавление, выбор и удаление
# элементов."

# Задача "Первые пользователи".

import sqlite3

# Создайте файл базы данных not_telegram.db и подключитесь к ней, используя
# встроенную библиотеку sqlite3.
conn = sqlite3.connect ( 'not_telegram.db' )
# Создайте объект курсора и выполните следующие действия при помощи SQL
# запросов:
cursor = conn.cursor ( )

# Создайте таблицу Users, если она ещё не создана. В этой таблице должны
# присутствовать следующие поля:
# id - целое число, первичный ключ
# username - текст (не пустой)
# email - текст (не пустой)
# age - целое число
# balance - целое число (не пустой)
cursor.execute (
        '''CREATE TABLE IF NOT EXISTS Users (
            id INTEGER PRIMARY KEY,
            username TEXT NOT NULL,
            email TEXT NOT NULL,
            age INTEGER,
            balance INTEGER NOT NULL
        )'''
        )

# Заполните её 10 записями:
# User1, example1@gmail.com, 10, 1000
# User2, example2@gmail.com, 20, 1000
# User3, example3@gmail.com, 30, 1000
# ...
# User10, example10@gmail.com, 100, 1000

for i in range ( 1, 11 ) :
    cursor.execute (
            "INSERT INTO Users(username, email, age, balance) VALUES (?, ?, "
            "?, ?)",
            (f'User{i}', f'example{i}@gmail.com', i * 10, 1000)
            )

conn.commit ( )

# Обновите balance у каждой 2ой записи начиная с 1ой на 500:
# User1, example1@gmail.com, 10, 500
# User2, example2@gmail.com, 20, 1000
# User3, example3@gmail.com, 30, 500
# ...
# User10, example10@gmail.com, 100, 1000

cursor.execute ( '''UPDATE Users SET balance = 500 WHERE id % 2 != 0''' )
conn.commit ( )

# Удалите каждую 3ую запись в таблице начиная с 1ой:
# User2, example2@gmail.com, 20, 1000
# User3, example3@gmail.com, 30, 500
# User5, example5@gmail.com, 50, 500
# ...
# User9, example9@gmail.com, 90, 500

cursor.execute ( '''DELETE FROM Users WHERE id % 3 = 1''' )
conn.commit ( )

# Сделайте выборку всех записей при помощи fetchall(),
# где возраст не равен 60 и выведите их в консоль в следующем формате (без id):
# Имя: <username> | Почта: <email> | Возраст: <age> | Баланс: <balance>

cursor.execute (
        'SELECT username, email, age, balance FROM Users WHERE age != 60'
        )
rows = cursor.fetchall ( )

for row in rows :
    print (
            f"Имя: {row [ 0 ]} | Почта: {row [ 1 ]} | Возраст: {row [ 2 ]} | "
            f"Баланс: {row [ 3 ]}"
            )

conn.close ( )

# Пример результата выполнения программы:
# Вывод на консоль:
# Имя: User2 | Почта: example2@gmail.com | Возраст: 20 | Баланс: 1000
# Имя: User3 | Почта: example3@gmail.com | Возраст: 30 | Баланс: 500
# Имя: User5 | Почта: example5@gmail.com | Возраст: 50 | Баланс: 500
# Имя: User8 | Почта: example8@gmail.com | Возраст: 80 | Баланс: 1000
# Имя: User9 | Почта: example9@gmail.com | Возраст: 90 | Баланс: 500

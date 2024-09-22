# ============================================================================

# Coding            : utf-8

# Script Name	    : Написание примитивной ORM
# File              : module_14_*.py

# Author			: Sergey Romanov
# Created			: 01.10.2024
# Last Modified	    : 01.10.2024
# Version			: 1.0.001

# Modifications	:
# Modifications	: 1.0.1 - Tidy up the comments and syntax

# Description       : aiogram script
# Description		: This will go through
#                     and backup all my automator services workflows

# ============================================================================

__author__ = 'Sergey Romanov'
__version__ = '1.0.001'

RSL_DEBUG = True

# module_16_3.py

# Домашнее задание по теме "CRUD Запросы: Get, Post, Put Delete."
# Цель: выработать навык работы с CRUD запросами.

from typing import Annotated

# Задача "Имитация работы с БД".
from fastapi import FastAPI, Path

# Создайте новое приложение FastAPI и сделайте CRUD запросы.
app = FastAPI ( )

# Создайте словарь users = {'1': 'Имя: Example, возраст: 18'}
users = { '1' : 'Имя: Example, возраст: 18' }


# Реализуйте 4 CRUD запроса:
# get запрос по маршруту '/users', который возвращает словарь users.
@app.get ( "/users" )
async def get_users ( ) :
    """

    @return:
    @rtype:
    """
    return users


# post запрос по маршруту '/user/{username}/{age}', который добавляет в
# словарь по максимальному по значению ключом
# значение строки "Имя: {username}, возраст: {age}". И возвращает строку
# "User <user_id> is registered".
@app.post ( "/user/{username}/{age}" )
async def add_user (
        username: Annotated [ str, Path (
                description = "Enter username",
                min_length = 5,
                max_length = 20,
                examples = "UrbanUser"
                ) ],
        age: Annotated [ int, Path (
                description = "Enter age",
                ge = 18,
                le = 120,
                examples = 24
                ) ]
        ) :
    """

    @param username:
    @type username:
    @param age:
    @type age:
    @return:
    @rtype:
    """
    new_user_id = str ( int ( max ( users.keys ( ) ) ) + 1 )
    users [ new_user_id ] = f"Имя: {username}, возраст: {age}"
    return { "message" : f"User {new_user_id} is registered" }


# put запрос по маршруту '/user/{user_id}/{username}/{age}',
# который обновляет значение из словаря users
# под ключом user_id на строку "Имя: {username}, возраст: {age}".
# И возвращает строку "The user <user_id> is registered"
@app.put ( "/user/{user_id}/{username}/{age}" )
async def update_user (
        user_id: Annotated [ int, Path (
                description = "Enter User ID",
                ge = 1, le = 100,
                examples = 1
                ) ],
        username: Annotated [ str, Path (
                description = "Enter username",
                min_length = 5,
                max_length = 20,
                examples = "UrbanProfi"
                ) ],
        age: Annotated [ int, Path (
                description = "Enter age",
                ge = 18, le = 120,
                examples = 28
                ) ]
        ) :
    """

    @param user_id:
    @type user_id:
    @param username:
    @type username:
    @param age:
    @type age:
    @return:
    @rtype:
    """
    user_id_str = str ( user_id )
    if user_id_str in users :
        users [ user_id_str ] = \
            f"Имя: {username}, возраст: {age}"
        return { "message" :
                     f"User {user_id_str} has been updated" }
    else :
        return { "error" :
                     f"User with ID {user_id_str} does not exist" }


# delete запрос по маршруту '/user/{user_id}',
# который удаляет из словаря
# users по ключу user_id пару.
@app.delete ( "/user/{user_id}" )
async def delete_user (
        user_id: Annotated [ int, Path (
                description = "Enter User ID",
                ge = 1,
                le = 100,
                examples = 2
                ) ]
        ) :
    user_id_str = str ( user_id )
    if user_id_str in users :
        del users [ user_id_str ]
        return { "message" :
                     f"User {user_id_str} has been deleted" }
    else :
        return { "error" :
                     f"User with ID {user_id_str} does not exist" }

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

# module_16_1.py

# Домашнее задание по теме "Основы Fast Api и маршрутизация"
# Цель: научиться создавать базовую маршрутизацию для обработки данных в
# FastAPI.

# Задача "Начало пути".

from typing import Optional

from fastapi import FastAPI

# Создайте приложение(объект) FastAPI
# предварительно импортировав класс для
# него.
app = FastAPI ( )


# Создайте маршрут к главной странице - "/".
# По нему должно выводиться
# сообщение "Главная страница".
@app.get ( "/" )
async def get_main_page ( ) :
    """

    @return:
    @rtype:
    """
    return { "message" : "Главная страница" }


# Создайте маршрут к странице администратора - "/user/admin".
# По нему должно выводиться сообщение "Вы вошли как администратор".
@app.get ( "/user/admin" )
async def get_admin_page ( ) :
    """

    @return:
    @rtype:
    """
    return { "message" : "Вы вошли как администратор" }


# Создайте маршрут к страницам пользователей используя параметр в пути -
# "/user/{user_id}".
# По нему должно выводиться сообщение "Вы вошли как пользователь № <user_id>".
@app.get ( "/user/{user_id}" )
async def get_user_number ( user_id: int ) :
    """

    @param user_id:
    @type user_id:
    @return:
    @rtype:
    """
    return { "message" : f"Вы вошли как пользователь № {user_id}" }


# Создайте маршрут к страницам пользователей передавая данные в адресной
# строке - "/user".
# По нему должно выводиться сообщение "Информация о пользователе. Имя:
# <username>, Возраст: <age>".
@app.get ( "/user" )
async def get_user_info ( username: str, age: Optional [ int ] = None ) :
    """

    @param username:
    @type username:
    @param age:
    @type age:
    @return:
    @rtype:
    """
    return {
            "message" :
            f"Информация о пользователе. Имя: {username}, "
            f"Возраст: {age if age else 'не указан'}"
            }

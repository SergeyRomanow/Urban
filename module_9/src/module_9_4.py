# ============================================================================
# Coding            : utf-8

# Script Name	    : ГЕНЕРАТОРНЫЕ_СБОРКИ
# File              : module_9_4.py

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

    СОЗДАНИЕ_ФУНКЦИЙ_НА_ЛЕТУ

    Задача "Функциональное разнообразие":

    Lambda-функция:
    Даны 2 строки:
    first = 'Мама мыла раму'
    second = 'Рамена мало было'

    Необходимо составить lambda-функцию для следующего выражения -

    list(map(?,first, second)).

    Здесь ? - место написания lambda-функции.

    Результатом должен быть список совпадения букв в той же позиции:

    [False, True, True, False, False, False, False, False, True, False, False,
    False, False, False]

    Где True - совпало, False - не совпало.

    Замыкание:

    Напишите функцию get_advanced_writer(file_name),
    принимающую название файла для записи.

    Внутри этой функции, напишите ещё одну - write_everything(*data_set),
    где: *data_set - параметр принимающий неограниченное количество данных
    любого типа.

    Логика write_everything заключается в добавлении в файл file_name всех
    данных из data_set в том же виде.
    Функция get_advanced_writer возвращает функцию write_everything.

    Данный код:

    write = get_advanced_writer('example.txt')
    write('Это строчка', ['А', 'это', 'уже', 'число', 5, 'в', 'списке'])

    Запишет данные в файл в таком виде:

    Метод __call__:

    Создайте класс MysticBall, объекты которого обладают атрибутом words
    хранящий коллекцию строк.

    В этом классе также определите метод __call__, который будет случайным
    образом выбирать слово из words и возвращать его.

    Для случайного выбора с одинаковой вероятностью для каждого данного
    в коллекции можете использовать функцию choice из модуля random.

    Ваш код (количество слов для случайного выбора может быть другое):
    from random import choice

    Ваш класс здесь:

    first_ball = MysticBall('Да', 'Нет', 'Наверное')
    print(first_ball())
    print(first_ball())
    print(first_ball())

    Примерный результат (может отличаться из-за случайности выбора):

    Да
    Да
    Наверное

"""
from __future__ import absolute_import
# from .__init__ import main
from codecs import open
from os import path

__author__ = 'Sergey Romanov'
__version__ = '1.0.001'

RSL_DEBUG = False

first = 'Мама мыла раму'
second = 'Рамена мало было'

result = list ( map ( lambda x, y : x == y, first, second ) )
print ( result )


def get_advanced_writer ( file_name ) :

    """
    get_advanced_writer
    """

    def write_everything ( *data_set ) :

        """
        write_everything
        """

        with open ( file_name, mode = 'w', encoding = 'utf-8' ) as fw :
            for item in data_set :
                item = str ( item ) + '\n'
                fw.write ( item )

    return write_everything


write = get_advanced_writer ( 'example.txt' )
write ( 'Это строчка',
        [ 'А', 'это', 'уже', 'число', 75, 'в', 'списке' ]
      )

from random import choice


class MysticBall :

    """
    MysticBall
    """

    def __init__ ( self, *words ) :
        self.words = words

    def __call__ ( self, *words ) :
        return choice ( self.words )


first_ball = MysticBall (
        'Без сомнений',
        'Возможно',
        'Да',
        'Думаю нет',
        'Мало шансов',
        'Не могу сказать',
        'Не сейчас',
        'Нет'
        'Неясно',
        'Очень вероятно',
        'Спросите позже',
        'Спросите снова',
        'Точно да',
        'Шансы хорошие',
        )

print ( first_ball ( ) )
print ( first_ball ( ) )
print ( first_ball ( ) )


def main ( *args, **kwargs ) :
    """
        Функция
        @:return result : int
    """
    result_ = int ( 0 )

    if RSL_DEBUG :
        print ( f'--->> Author module:\t\t{__author__}.' )
        print ( f'--->>Version:\t\t{__version__}.' )
    else :
        return result_

    if args >= 5 :
        return exit ( 1 )

    return None


if __name__ == '__main__' :
    main ( )

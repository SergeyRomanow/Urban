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
Генераторы

Напишите функцию-генератор all_variants(text),
которая принимает строку text и возвращает объект-генератор,
при каждой итерации которого будет возвращаться
подпоследовательности переданной строки.

Напишите функцию-генератор all_variants(text).

Опишите логику работы внутри функции all_variants.

Вызовите функцию all_variants и выполните итерации.

Пример результата выполнения программы:

Пример работы функции:

a = all_variants("abc")
for i in a:
print(i)

"""
from __future__ import absolute_import


def all_variants ( text ) :
    """
    """
    for symbol_x in range ( len ( text ) ) :
        for symbol_y in range ( len ( text ) - symbol_x ) :
            yield text [ symbol_y :symbol_y + symbol_x + 1 ]


for value in all_variants ( "abc" ) :
    print ( value )

# Вывод на консоль:
# a
# b
# c
# ab
# bc
# abc

# from .__init__ import main

__author__ = 'Sergey Romanov'
__version__ = '1.0.001'

RSL_DEBUG = False


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

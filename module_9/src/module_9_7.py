# ============================================================================

# Coding            : utf-8

# Script Name	    : Декораторы
# File              : module_9_*.py

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
Практическое задание

2023/12/05 00:00|Домашнее задание по теме "Декораторы"

Задание: Декораторы в Python

Цель задания:

Освоить механизмы создания декораторов Python.
Практически применить знания,
создав функцию декоратор и обернув ею другую функцию.

Задание:

Напишите 2 функции:

Функция, которая складывает 3 числа (sum_three)
Функция декоратор (is_prime), которая распечатывает "Простое",
если результат 1ой функции будет простым числом и "Составное"
в противном случае.

Пример:

result = sum_three(2, 3, 6)
print(result)

Результат консоли:
Простое
11

Примечания:
Не забудьте написать внутреннюю функцию wrapper в is_prime
Функция is_prime должна возвращать wrapper
@is_prime - декоратор для функции sum_three

Файл module_9_7.py и загрузите его на ваш Git"""
from __future__ import absolute_import
# from .__init__ import main

__author__ = 'Sergey Romanov'
__version__ = '1.0.001'

RSL_DEBUG = False


def is_prime ( func ) :
    """
    """

    def wrapper ( *numbers ) :
        summation = func ( *numbers )
        count = 0
        for element in range ( 1, summation + 1 ) :
            if summation % element == 0 :
                count += 1
        if count > 2 :
            return f'Составное \n{summation}'
        if count == 2 :
            return f'Простое \n{summation}'

    return wrapper


@is_prime
def sum_three ( *numbers ) :
    """
    """
    return sum ( numbers )


result = sum_three ( 2, 3, 6 )
print ( result )


# Результат консоли:
# Простое
# 11

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

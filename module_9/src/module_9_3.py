# ============================================================================
# Coding            : utf-8


# Script Name	    : ГЕНЕРАТОРНЫЕ_СБОРКИ
# File              : module_9_3.py

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

    2023/12/01 00:00|Домашнее задание по теме "Генераторные сборки"

    Если вы решали старую версию задачи, проверка будет производиться по ней.
    Ссылка на старую версию тут.

    ЦЕЛЬ:

    понять механизм создания генераторных сборок и и
    спользования встроенных функций-генераторов.

    ЗАДАЧА:

    Дано 2 списка:
    first   = ['Strings', 'Student', 'Computers']
    second  = ['Строка', 'Урбан', 'Компьютер']

    Необходимо создать 2 генераторных сборки:

    В переменную first_result запишите генераторную сборку,
    которая высчитывает разницу длин строк из списков first и second,
    если их длины не равны.
    Для перебора строк попарно из двух списков используйте функцию zip.

    В переменную second_result запишите генераторную сборку,
    которая содержит результаты сравнения длин строк в одинаковых позициях
    из списков first и second.

    Составьте эту сборку НЕ используя функцию zip.

    Используйте функции range и len.

    Пример результата выполнения программы:

    Пример выполнения кода:

    print(list(first_result))
    print(list(second_result))

    Вывод в консоль:

    [1, 2]
    [False, False, True]

    Примечания:
    Это небольшая практика, поэтому важность выполнения каждого
    условия обязательна.

"""

# ============================================================================

from __future__ import absolute_import

__author__ = 'Sergey Romanov'
__version__ = '1.0.001'
RSL_DEBUG = False

first = [ 'Strings', 'Student', 'Computers' ]
second: list [ str ] = [ 'Строка', 'Урбан', 'Компьютер' ]

first_result = \
    (
            (len ( item1 ) - len ( item2 ))
            for item1, item2 in zip ( first, second )
            if len ( item1 ) != len ( item2 )
            )

print ( list ( irst_result ) )

second_result = \
    (
            len ( first [ item1 ] ) == len ( second [ item2 ] )
            for item1 in range (
        len ( first )
        )
            for item2 in range ( len ( second ) ) if item1 == item2)

print ( list ( second_result ) )


# ============================================================================
# Пример результата выполнения программы:

# Пример выполнения кода:

# print(list(first_result))
# print(list(second_result))

# Вывод в консоль:

# [1, 2]
# [False, False, True]

def main ( *args, **kwargs ) :
    """
        Функция
        @:return result : int
    """
    result = int ( 0 )

    if RSL_DEBUG :
        print ( f'--->> Author module:\t\t{__author__}.' )
    else :
        return result

    if args >= 5 :
        return exit ( 1 )

    return None


if __name__ == '__main__' :
    main ( )

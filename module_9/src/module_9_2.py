# ============================================================================
# Coding            : utf-8

# Script Name	    : backup_automate_services.py
# File              : main.py

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
Практическое задание:2023/11/30 00:00|

Домашнее задание по теме "Списковые, словарные сборки"
Если вы решали старую версию задачи, проверка будет производиться по ней.
Ссылка на старую версию тут.

ЦЕЛЬ:

закрепить знания о списочных и словарных сборках,
решив несколько небольших задач.

ЗАДАЧА:

Даны несколько списков, состоящих из строк:

first_strings =
[
'Elon','Musk', 'Programmer', 'Monitors', 'Variable'
]
second_strings =
[
'Task','Git', 'Comprehension', 'Java', 'Computer', 'Assembler'
]

В переменную FIRST_RESULT запишите список,
созданный при помощи сборки состоящий из длин строк списка first_strings,
при условии, что длина строк не менее 5 символов.

В переменную SECOND_RESULT запишите список созданный при помощи
сборки состоящий из пар слов(кортежей) одинаковой длины.

Каждое слово из списка first_strings должно сравниваться
с каждым из second_strings. -- (два цикла)

В переменную third_result запишите словарь созданный при помощи
сборки, где парой ключ-значение будет строка-длина строки.

Значения строк будут перебираться из объединённых вместе списков
first_strings и second_strings.

Условие записи пары в словарь - чётная длина строки.

Пример результата выполнения программы:
Пример выполнения кода:
print(first_result)
print(second_result)
print(third_result)

Вывод на консоль:

[10, 8, 8]

[('Elon', 'Task'), ('Elon', 'Java'), ('Musk', 'Task'),
 ('Musk', 'Java'), ('Monitors', 'Computer'),
 ('Variable', 'Computer')
]

{'Elon': 4, 'Musk': 4, 'Programmer': 10,
 'Monitors': 8, 'Variable': 8, 'Task': 4,
 'Java': 4, 'Computer': 8
}

Примечания:
Помните, когда вы используете 2 цикла for внутри сборки,
первый цикл - внешний, второй - внутренний.

"""


print('СПИСКОВЫЕ, СЛОВАРНЫЕ_СБОРКИ')

# Даны несколько списков, состоящих из строк first_strings = ['Elon',
# 'Musk', 'Programmer', 'Monitors', 'Variable'] second_strings = ['Task',
# 'Git', 'Comprehension', 'Java', 'Computer', 'Assembler'] В переменную
# first_result запишите список созданный при помощи сборки состоящий из длин
# строк списка first_strings, при условии, что длина строк не менее 5
# символов. В переменную second_result запишите список созданный при помощи
# сборки состоящий из пар слов(кортежей) одинаковой длины. Каждое слово из
# списка first_strings должно сравниваться с каждым из second_strings. (два
# цикла) В переменную third_result запишите словарь созданный при помощи
# сборки, где парой ключ-значение будет строка-длина строки. Значения строк
# будут перебираться из объединённых вместе списков first_strings и
# second_strings. Условие записи пары в словарь - чётная длина строки.
# Пример результата выполнения программы: Пример выполнения кода: print(
# first_result) print(second_result) print(third_result)


first_strings = \
    [
        'Elon',
        'Musk',
        'Programmer',
        'Monitors',
        'Variable'
    ]

second_strings = \
    [
        'Task',
        'Git',
        'Comprehension',
        'Java',
        'Computer',
        'Assembler'
    ]

print('\nСписок, состоящий из длин строк списка '
      'first_strings, длина строк не менее 5 символов')
first_result = [len(item)
                for item in first_strings
                if len(item) >= 5
                ]
print(first_result)

print('\nСписок, состоящий из пар слов(кортежей) '
      'одинаковой длины слов из списков first_strings, second_strings')
second_result = [(item1, item2)
                 for item1 in first_strings
                 for item2 in second_strings
                 if len(item1) == len(item2)
                 ]
print(second_result)
#
print('\nСловарь, ключ '
      '- строка: значение '
      '- длина строки (чётная длина строки, '
      'списки first_strings и second_strings'
      )
third_result = {item: len(item)
                for item in first_strings + second_strings
                if len(item) % 2 == 0
                }
print(third_result)

# Вывод на консоль: [10, 8, 8]
# [
# ('Elon', 'Task'), ('Elon', 'Java'), ('Musk',# 'Task'),
# ('Musk', 'Java'),
# ('Monitors', 'Computer'),
# 'Variable',# 'Computer')
# ]

# {
# 'Elon': 4,
# 'Musk': 4,
# 'Programmer': 10,
# 'Monitors': 8,
# 'Variable': 8,
# 'Task': 4, 'Java': 4,
# 'Computer': 8
# }

# СТАРАЯ_ВЕРСИЯ
# Дан список целых чисел, примените функции map и filter так,
# что бы в конечном списке оставить нечётные квадраты чисел
# Не забывайте, что встроенные функции map и filter возвращают генератор,
# сами операции преобразования не выполняются.

# ВХОДНЫЕ_ДАННЫЕ
# [1, 2, 5, 7, 12, 11, 35, 4, 89, 10]

# ВЫХОДНЫЕ_ДАННЫЕ
# [1, 25, 49, 121, 1225, 7921]


print('\nСтарая версия задания: \nmap и filter =>> в результате нечётные '
      'квадраты чисел')


def sqrt(x):
    return x ** 2


def add_even_numbers(x):
    return x % 2


list_ = [1, 2, 5, 7, 12, 11, 35, 4, 89, 10]

list_new = map(sqrt, filter(add_even_numbers, list_))
print(list(list_new))

print('\nгенерация списка =>> в результате нечётные квадраты чисел')

result2 = [item ** 2 for item in list_ if item % 2 != 0]
print(result2)

# ==========================================
# Coding: utf-8
# (c) 2024 Copyright Reserved RSL Studio LLC
# License: MIT
#
# МОДУЛЬ 9: Функциональный стиль в программировании
# ==========================================
"""
    МОДУЛЬ 9: функциональное программирование
    Домашнее задание по теме:
    \"Введение в функциональное программирование\"
"""

RSL_NAME_AUTHOR = "ROMANOV SERGEY"
RSL_DEBUG = True

RSL_DATA_TASK = """
 "Call at once"
 
Напишите функцию apply_all_func(int_list, *functions), 
которая принимает параметры:
int_list - список из чисел (int, float)
*functions - неограниченное кол-во функций 
(которые применимы к спискам, состоящим из чисел)

Эта функция должна:

Вызвать каждую функцию к переданному списку int_list
Возвращать словарь, где ключом будет название вызванной функции,
а значением - её результат работы со списком int_list.

Пункты задачи:

В функции apply_all_func создайте пустой словарь results.
Переберите все функции из *functions.
При переборе функций записывайте в словарь results 
результат работы этой функции под ключом её названия.
Верните словарь results.
Запустите функцию apply_all_func, 
передав в неё список из чисел и набор других функций.

"""

_list_int = [ ]


def get_names_russian ( ) :
    return [ 'Ваня', 'Коля', 'Маша', ]


def apply_all_func ( _list_int, *functions ) :
    list_results = [ ]

    for item in functions :
        print ( f'--->> List: {item()}.' )
        list_results.append ( item() )

        if RSL_DEBUG :

            print ( f'--->> list_results: {list_results}.' )

    return list_results


# # Имя функции указывает на обьект функции. Обычная переменная.
# print ( type ( get_names_russian ) )
# # можно узнать название функции
# print ( get_names_russian.__name__ )
#

def main ( ) :

    """
        Функция я
        @:params
        @:return result : int
        :rtype: object
    """

    result = int ( 0 )

    if RSL_DEBUG :

        apply_all_func ( _list_int,
                         get_names_russian )

        # print (
        #         f'--->> Author module: '
        #         f'{RSL_NAME_AUTHOR}.'
        #         )
        # result += result + 1
    else :
        return result

    return None


if __name__ == '__main__' :
    main ( )

"""
def apply_all_func(int_list, *functions):
    results = {}
    for func in functions:
        results[func.__name__] = func(int_list)
    print(results)


apply_all_func([6, 20, 15, 9,45], max, min)
apply_all_func([6, 20, 15, 9], len, sum, sorted)
""'

# ============================================================================
# Coding            : utf-8
from __future__ import absolute_import

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

description_ = """\
Создайте пользовательский класс исключения StepValueError, который наследуется 
от ValueError.

Наследования достаточно, класс оставьте пустым при помощи оператора pass.
Создайте класс Iterator, который обладает следующими свойствами:

Атрибуты объекта:
    start - целое число с которого начинается итерация.
    stop - целое число на котором заканчивается итерация.
    step - шаг с которой совершается итерация.
    pointer - указывает на текущее число в итерации (изначально start)

Методы:

__init__(self, start, stop, step=1) - принимающий значения старта 
и конца итерации, а также шага.
В этом методе в первую очередь проверяется step на равенство 0.
Если равно, то выбрасывается исключение StepValueError
('шаг не может быть равен 0')

__iter__ - метод сбрасывающий значение pointer на start 
и возвращающий сам объект итератора.

__next__ - метод увеличивающий атрибут pointer на step.
В зависимости от знака атрибута step итерация завершиться либо
когда pointer станет больше stop,
либо меньше stop. Учтите это при описании метода.

Пункты задачи:

Создайте класс исключения StepValueError.
Создайте класс Iterator и опишите его атрибуты и методы.
Создайте несколько объектов класса Iterator и совершите итерации 
с ними при помощи цикла for.
"""


class StepValueError ( ValueError ) :

    """
    class StepValueError
    """
    pass


class Iterator :

    """
    class Iterator:
    """

    def __init__ ( self, start, stop, step = 1 ) :

        """
        def __init__
        """

        self.pointer = 0
        self.start = start
        self.stop = stop
        self.step = step
        if step == 0 :
            raise StepValueError ( )

    def __iter__ ( self ) :

        """

        """

        self.pointer = self.start - self.step
        return self

    def __next__ ( self ) :

        """

        """

        self.pointer += self.step
        if (self.step > 0 and self.pointer > self.stop or self.step < 0 and
                self.pointer < self.stop) :
            raise StopIteration ( )
        return self.pointer


print ( 'Старая версия задания' )

descript_1 = """\
Напишите класс - итератор EvenNumbers для перебора чётных чисел 
в определённом числовом диапазоне.

При создании и инициализации объекта этого класса создаются атрибуты:

    start – начальное значение (если значение не передано, то 0)
    end – конечное значение (если значение не передано, то 1)
    
"""


class EvenNumbers :

    """
    class EvenNumbers :
    """

    def __init__ ( self, start = 0, end = 1 ) :

        """
        def __init__
        """

        self.start = start
        self.end = end

    def __iter__ ( self ) :
        """

        """
        if self.start % 2 == 0 :
            self.start -= 2
            return self
        if self.start % 2 != 0 :
            self.start -= 1
            return self

    def __next__ ( self ) :
        """

        """
        self.start += 2
        if self.start > self.end :
            raise StopIteration ( )
        return self.start


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


try :
    iter1 = Iterator ( 100, 200, 0 )
    for i in iter1 :
        print ( i, end = ' ' )
except StepValueError :
    print ( 'Шаг указан неверно' )

iter2 = Iterator ( -5, 1 )
iter3 = Iterator ( 6, 15, 2 )
iter4 = Iterator ( 5, 1, -1 )
iter5 = Iterator ( 10, 1 )

for i in iter2 :
    print ( i, end = ' ' )
print ( )
for i in iter3 :
    print ( i, end = ' ' )
print ( )
for i in iter4 :
    print ( i, end = ' ' )
print ( )
for i in iter5 :
    print ( i, end = ' ' )
print ( )

# Вывод на консоль:
# Шаг указан неверно
# -5 -4 -3 -2 -1 0 1
# 6 8 10 12 14
# 5 4 3 2 1

en = EvenNumbers ( 10, 25 )
for i in en :
    print ( i )

# Выходные данные
# После перебора и вывода:
# 10
# 12
# 14
# 16
# 18
# 20
# 22
# 24


if __name__ == '__main__' :
    main ( )

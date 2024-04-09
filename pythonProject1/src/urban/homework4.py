# Модуль 'homework4.py'
# Практическое задание по теме: "Неизменяемые и изменяемые объекты. Кортежи и списки"

# Цель:
# Написать программу на языке Python, используя Pycharm, для работы с неизменяемыми и изменяемыми объектами.

# 1. В проекте, где вы решаете домашние задания, создайте модуль 'homework4.py' и напишите весь код в нём.

# 2. Задайте переменные разных типов данных:
#   - Создайте переменную immutable_var и присвойте ей кортеж из нескольких элементов разных типов данных.
#   - Выполните операции вывода кортежа immutable_var на экран.

# 3. Изменение значений переменных:
#   - Попытайтесь изменить элементы кортежа immutable_var. Объясните, почему нельзя изменить значения элементов кортежа.

# 4. Создание изменяемых структур данных:
#   - Создайте переменную mutable_list и присвойте ей список из нескольких элементов.
#   - Измените элементы списка mutable_list.
#   - Выведите на экран измененный список mutable_list.

# Переменная с данными для кортежа и списка
var_0 = 1
var_1 = 2.01
var_2 = 'СТРОКА'
var_3 = True
print()
print(f"{'var_0' : <10}{'var_1' : <10}{'var_2' : <10}{'var_3' : <10}")
print(f"{var_0 : <10}{var_1 : <10}{var_2 : <10}{var_3 : <10}")

value = var_0, var_1, var_2, var_3
size_of_value = value.__sizeof__()  # размер в памяти
size_value = len(value)

# printing values of variables in Aligned manner
# for i in range(0, size_value - 1):
#     print(f"{'var_0' : <10}{'var_1' : <10}{'var_2' : <10}{'var_3' : <10}")
#     print(f"{value[i] : <10}{value[i] : ^10}{value[i] : ^10}{value[i] : >5}")



print()

print("--->>> ПЕРЕМЕННАЯ {value} | Тип: ", type(value), "| Размер: ", size_value, "| __sizeof__: ", size_value)
print("--->>> элементы 0: ", type(var_0), "| ЗНАЧЕНИЕ: ", var_0)
print("--->>> элементы 1: ", type(var_1), "| ЗНАЧЕНИЕ: ", var_1)
print("--->>> элементы 2: ", type(var_2), "| ЗНАЧЕНИЕ: ", var_2)
print("--->>> элементы 3: ", type(var_3), "| ЗНАЧЕНИЕ: ", var_3)
print()

# _tuple = value                          # immutable_var     - кортеж (tuple) не изменяемый
# _tuple = (value)                          # immutable_var     - кортеж (tuple) не изменяемый
_tuple = tuple(value)  # immutable_var     - кортеж (tuple) не изменяемый
_tuple_m = (value, [value])  # tuple mutable     - кортеж (tuple) изменяемый внутри
size_tuple = _tuple.__sizeof__()  # размер в памяти
size_tuple_m = _tuple_m.__sizeof__()

print("--->>> Кортеж: Тип: ", type(_tuple), "Размер: ", size_tuple)
print("--->>> Кортеж: ", _tuple)
print()

print("--->>> Кортеж M: Тип: ", type(_tuple_m), 'Размер:', size_tuple_m)
print("--->>> Кортеж M: ", _tuple_m)
print("--->>> Кортеж M: Значение [0]-[3] =", _tuple_m[0][3], "| Значение 2М = ", _tuple_m)
print()

print("--->>> 3. Изменение значений переменных:")
print("--->>> Если мы захотим изменить этот элемент _tuple_m[0][3], например на 'VALUE'")
print("--->>> попросим вывести кортеж на экран, то столкнемся с ошибкой (Рис.6).")
# _tuple_m[0][3] = 'VALUE'
print("--->>> _tuple_m[0][3] = 'VALUE' ")
print("--->>> TypeError: 'tuple' object does not support item assignment")
print("--->>> TypeError: объект 'tuple' не поддерживает назначение элементов")
print("--->>> Ошибка буквально сообщает нам, что кортеж не поддерживает обращение по элементам.")
print()

# _list = [value]  # mutable_list      - список (list)
_list = list(value)  # mutable_list      - список (list)
size_list = _list.__sizeof__()
print("--->>> Список: Тип: ", type(_list), 'Размер:', size_list)
print("--->>> Список: ", _list)
_list[2] = "VALUE"
print("--->>> Список: ", _list, "ЗАМЕНА ЗНАЧЕНИЯ ПРОИЗВЕДЕНА")

# size_list = len(_list)


# print("--->>> Кортеж M (размер в памяти): ", size_tuple_m)

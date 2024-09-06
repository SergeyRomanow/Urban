
# Введение в функциональное программирование
# Напишите функцию apply_all_func(int_list, *functions),
# которая принимает параметры:
# int_list - список из чисел (int, float)
# *functions - неограниченное кол-во функций (которые применимы
# к спискам, состоящим из чисел)
# Эта функция должна:
# Вызвать каждую функцию к переданному списку int_list
# Возвращать словарь, где ключом будет название вызванной функции,
# а значением - её результат работы со списком int_list.
# Пункты задачи:
# В функции apply_all_func создайте пустой словарь results.
# Переберите все функции из *functions.
# При переборе функций записывайте в словарь results результат работы
# этой функции под ключом её названия.
# Верните словарь results.
# Запустите функцию apply_all_func, передав в неё список из чисел
# и набор других функций.
# Пример результата выполнения программы:
# В примере используются следующие функции:
# min - принимает список, возвращает минимальное значение из него.
# max - принимает список, возвращает минимальное значение из него.
# len - принимает список, возвращает кол-во элементов в нём.
# sum - принимает список, возвращает сумму его элементов.
# sorted - принимает список, возвращает новый отсортированный
# список на основе переданного.


def apply_all_func(int_list, *functions):
    results = {}

    for item in int_list:
        try:
            for item, val in enumerate(int_list):
                val = float(val)
                if val == int(val):
                    val = int(val)
                int_list[item] = val
                if val == bool(val):
                    int_list.remove(val)
        except ValueError:
            int_list.remove(val)

    for function in functions:
        results[function.__name__] = function(int_list)
    return results


print('Пример работы кода:')
print(apply_all_func([6, 20, 15, 9], max, min))
print(apply_all_func([6, 20, 15, 9], len, sum, sorted))
print()

# Вывод на консоль:
# {'max': 20, 'min': 6} {'len': 4, 'sum': 50, 'sorted': [6, 9, 15, 20]}

print(f'проверка на строковые значения и значения {bool}'
      f' с изменением длины списка '
      f'после удаления значений, не относящимся к {int}, {float}')

print(apply_all_func([6, '20.1', '15', 'True'],
                     max, min, len, sorted, sum))
print(apply_all_func([6, '20.5', 15.7, '9', False],
                     max, min, len, sorted, sum))


def main ( *args, **kwargs ) :

    """
        Функция исп
    """
    return None


if __name__ == '__main__':
    main()

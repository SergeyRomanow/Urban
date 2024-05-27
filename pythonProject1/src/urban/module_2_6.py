# 2023/10/05 00:00|Домашняя работа по уроку "Пространство имен и способы вызова функции"
# Цель: закрепить знание использования параметров в функции и знания из предыдущих модулей.
#
# Задача("Однокоренные"):
# Напишите функцию single_root_words, которая принимает одно обязательное слово в параметр root_word,
# а далее неограниченную последовательность в параметр *other_words.
# Функция должна составить новый список same_words только из тех слов списка other_words,
# которые содержат root_word или наоборот root_word содержит одно из этих слов.
# После вернуть список same_words в качестве результата своей работы.
#
# Пункты задачи:
# Объявите функцию single_root_words и напишите в ней параметры root_world и *other_words.
# Создайте внутри функции пустой список same_words, который пополнится нужными словами.
# При помощи цикла for переберите предполагаемо подходящие слова.
# Пропишите корректное относительно задачи условие, при котором добавляются слова в результирующий список same_words.
# После цикла верните образованный функцией список same_words.
# Вызовите функцию single_root_words и выведете на экран(консоль) возвращённое ей занчение.
# Пример результата выполнения программы:
# Исходный код:
# result1 = single_root_words('rich', 'richiest, 'orichalcum', 'cheers', 'richies')
# result2 = single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel')
# print(result1)
# print(result2)
# Вывод на консоль:
# ['richiest', 'orichalcum', 'richies']
# ['Able', 'Disable']
# Примечания:
# При проверке наичлия одного слова в составе другого стоит учесть,
# что регистр символов не должен влять ни на что. ('Disablement' - 'Able')
# В сосновном в этой задаче вам понадобяться методы строк: count() и lower()/upper().
#
def single_root_words(root_world, *other_words):
    same_worlds = [root_world]
    # print(type(root_world))
    # print(type(other_words))
    for world in other_words:
        # print('-->>', 2)
        # print('-->>', world)
        # _find = root_world.find(world)
        if set(root_world) <= set(world):
            same_worlds.append(world)
            # continue
    return same_worlds
    print('--->>> List: ', same_worlds)

result1 = single_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'riches')
print(result1)

result2 = single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel')
print(result2)




# 1) Создать список из 20 случайных целых чисел в диапазоне от 1 до 100.
# Задание можно выполнить и через обычный цикл и через генератор списков.
import random
# new_list = []
# for i in range(20):
#     new_list.append(random.randint(1, 100))
#
# print(new_list)
#
# a = [random.randint(1, 100) for i in range(20)]
# print(a)

# 2) Создать словарь triangle в который записать точки A B C (ключи),
# и их координаты - кортежи (значения), созданные случайным образом с помощью модуля random в диапазоне от -10 до 10 по каждой оси.


# def create_random_point():
#     point = (random.randint(-10, 10),
#              random.randint(-10, 10),
#              random.randint(-10, 10))
#     return point
# def create_line_segment():
#     line_segment = {"A": create_random_point(),
#                     "B": create_random_point(),
#                     "C": create_random_point()}
#     return line_segment
# def print_line_segment(line_segment):

# triangle = {"A": (), "B": (), "C": ()}
# for key in triangle:
#     triangle[key] = tuple([random.randint(-100, 100) for i in range(3)])


triangle = {"A" : {(random.randint(-10, 10),
                    random.randint(-10, 10),
                    random.randint(-10, 10))
                   },
            "B" : {(random.randint(-10, 10),
                    random.randint(-10, 10),
                    random.randint(-10, 10))
                   },
            "C" : {(random.randint(-10, 10),
                    random.randint(-10, 10),
                    random.randint(-10, 10))
                   }}
print(triangle)

# 3) Создать функцию my_print, которая принимает в виде параметра строку и печатает ее
# с тремя символами * вначале и в конце строки.
# Пример:
# my_str = 'I'm the string'
# Печатает ***I'm the string***

my_str = "I'm the string"
def my_print(my):
    print(f'***{my}***')

my_print(my_str)

# 4) Дан список словарей persons в формате [{"name": "John", "age": 15}, ... ,{"name": "Jack", "age": 45}]

# person1 = {"name": "John",
#            "age": 15}
# person2 = {"name": "Jack",
#            "age": 45}
# person3 = {"name": "Sirius",
#            "age": 15}
# person4 = {"name": "Ruby",
#            "age": 18}
# person5 = {"name": "Bill",
#            "age": 46}
# person6 = {"name": "Ronda",
#            "age": 34}
# person7 = {"name": "Sirius",
#            "age": 29}
#




# а) Напечатать имя самого молодого человека. Если возраст совпадает - напечатать все имена.
# б) Напечатать самое длинное имя. Если длина имени совпадает - напечатать все имена.
# в) Посчитать среднее количество лет всех людей из списка.
#


# 5) Даны два словаря my_dict_1 и my_dict_2.
# а) Создать список из ключей, которые есть в обоих словарях.
# б) Создать список из ключей, которые есть в первом, но нет во втором словаре.
# в) Создать новый словарь из пар {ключ:значение}, для ключей, которые есть в первом, но нет во втором словаре.
# г) Объединить эти два словаря в новый словарь по правилу:
# если ключ есть только в одном из двух словарей - поместить пару ключ:значение,
# если ключ есть в двух словарях - поместить пару {ключ: [значение_из_первого_словаря, значение_из_второго_словаря]},
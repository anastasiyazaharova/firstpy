# 1) Создать список из 20 случайных целых чисел в диапазоне от 1 до 100.
# Задание можно выполнить и через обычный цикл и через генератор списков.
import random
new_list = []
for i in range(20):
    new_list.append(random.randint(1, 100))

print(new_list)

a = [random.randint(1, 100) for i in range(20)]
print(a)

########################################################################################################################

# 2) Создать словарь triangle в который записать точки A B C (ключи),
# и их координаты - кортежи (значения), созданные случайным образом с помощью модуля random в диапазоне от -10 до 10 по каждой оси.


# triangle = {"A": (), "B": (), "C": ()}
# for key in triangle:
#     triangle[key] = tuple([random.randint(-10, 10) for i in range(3)])

########################################################################################################################

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

########################################################################################################################

# 3) Создать функцию my_print, которая принимает в виде параметра строку и печатает ее
# с тремя символами * вначале и в конце строки.
# Пример:
# my_str = 'I'm the string'
# Печатает ***I'm the string***

my_str = "I'm the string"
def my_print(my):
    print(f'***{my}***')

my_print(my_str)

########################################################################################################################

# 4) Дан список словарей persons в формате [{"name": "John", "age": 15}, ... ,{"name": "Jack", "age": 45}]

persons = [{"name": "John", "age": 15},
           {"name": "Jack", "age": 45},
           {"name": "Sirius", "age": 15},
           {"name": "Ruby","age": 18},
           {"name": "Bill", "age": 46},
           {"name": "Ronda","age": 34},
           {"name": "Sirius", "age": 29}
           ]


# а) Напечатать имя самого молодого человека. Если возраст совпадает - напечатать все имена.

test_list = []
for x in persons:
    test_list.append(x["age"])
test_list.sort()
for x in persons:
    if x["age"] == test_list[0]:
        print("shortest " + x["name"])


# б) Напечатать самое длинное имя. Если длина имени совпадает - напечатать все имена.

for x in persons:
    if x["age"] == test_list[-1]:
        print("longest " + x["name"])

# в) Посчитать среднее количество лет всех людей из списка.

average_age = 0
for i in test_list:
    average_age += i
average_age /= len(test_list)

print(int(average_age))


# 5) Даны два словаря my_dict_1 и my_dict_2.

dict1 = {"one": "1",
         "two": "2",
         "tree": "3"}
dict2 = {"tree": "3",
         "four": "4",
         "five": "5"}

# а) Создать список из ключей, которые есть в обоих словарях.

list5 = []
for x in dict1:
    if x in dict2:
        list5.append(x)

print(list5)
# б) Создать список из ключей, которые есть в первом, но нет во втором словаре.

list5 = []
for x in dict1:
    if x not in dict2:
        list5.append(x)

print(list5)

# в) Создать новый словарь из пар {ключ:значение}, для ключей, которые есть в первом, но нет во втором словаре.

list_keys2 = []
new_dict = {}

for c in dict1:
    if c not in dict2:
        list_keys2.append(c)
        new_dict.update({c : dict1[c]})

print(list_keys2)
print(new_dict)

# г) Объединить эти два словаря в новый словарь по правилу:
# если ключ есть только в одном из двух словарей - поместить пару ключ:значение,
# если ключ есть в двух словарях - поместить пару {ключ: [значение_из_первого_словаря, значение_из_второго_словаря]},

list_keys3 = []
new_dict2 = {}

new_dict2.update(dict1)
new_dict2.update(dict2)

for b in dict1:
    if b in dict2:
        new_dict2[b] = [dict1[b], dict2[b]]

print(new_dict2)
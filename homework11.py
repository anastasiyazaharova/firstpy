# Задания
# data.json - файл с данными о некоторых математиках прошлого.
# 1. Необходимо написать функцию, которая считает эти данные из файла. Параметр функции - имя файла.

import json
import re


def read_data_json(filename):
    with open(filename, 'r', encoding='utf=8') as json_file:
        return json.load(json_file)


data = read_data_json("data.json")

# 2. Написать функцию сортировки данных по ФАМИЛИИ в поле "name" (у тех у кого она есть).
# Например для Rene Descartes фамилия это Descartes, у Pierre de Fermat - Fermat и т.д.
# Если фамилии нет, то использовать имя, например Euclid.


def key_sorted_by_name(obj_dict):
    if len(obj_dict["name"].split(' ')) == 1:
        return obj_dict["name"].split(' ')[0]
    else:
        return obj_dict["name"].split(' ')[-1]



new_sorted_data = sorted(data, key=key_sorted_by_name)
print(new_sorted_data)


# 3. Написать функцию сортировки по дате смерти из поля "years".
# Обратите внимание на сокращение BC. - это означает до н.э.

def key_sorted_by_data_death(obj_dict):
    year_death = re.findall(r'\d+', obj_dict["years"])
    if "BC" in obj_dict["years"]:
        return int(year_death[-1]) * -1
    else:
        return int(year_death[-1])


new_sorted_data_death = sorted(data, key=key_sorted_by_data_death)
print(new_sorted_data_death)


# 4. Написать функцию сортировки по количеству слов в поле "text"

def key_sorted_by_count_text(obj_dict):
    count_text = (obj_dict["text"]).split(" ")
    return len(count_text)


new_sorted_count_text = sorted(data, key=key_sorted_by_count_text)
print(new_sorted_count_text)
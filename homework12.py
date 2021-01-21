# Все пункты сделать как отдельные функции(можно создавать дополнительные вспомагательные функции)
#
# 1. Написать функцию, которая принимает в виде параметра целое число - количество цитат (см. урок 12).
# Надо получить ровно столько не повторяющихся цитат с данными и сохранить их в csv файл
# (имя файла сделать параметром по умолчанию).
# Заголовки файла:
# Author, Quote, URL. Если автор не указан, цитату не брать.
# Перед сохранением в csv, записи отсортировать по автору (в алфавитном порядке).

import requests
import csv
import re
import json

def get_uniq_q_in_list(count):
    url = "http://api.forismatic.com/api/1.0/"
    params = {"method": "getQuote",
              "format": "json",
              "key": 1,
              "lang": "ru"
    }
    file = []
    while len(file) < count:
        r = (requests.get(url, params=params)).json()
        if (not r in file) and (r["quoteAuthor"] != ''):
            file.append(r)
    return file

def write_csv_file(data, filename="text.csv"):
    data1 = sorted(data, key=lambda x: x.get("quoteAuthor"))
    with open(filename, 'w', encoding='utf=8') as csv_file:
        data = ["quoteAuthor", "quoteText", "quoteLink"]
        headers = {'quoteAuthor': 'Author', 'quoteText': 'Quote', 'quoteLink': 'URL'}
        writer = csv.DictWriter(csv_file, fieldnames=data, extrasaction='ignore')
        writer.writerow(headers)
        for row in data1:
            writer.writerow(row)

#write_csv_file(get_uniq_q_in_list(23))


# 2. Дан файл authors.txt
# 2.1) написать функцию, которая считывает данные из этого файла,
# возвращая СПИСОК тех строк в которых есть полная дата, писатель и указание на его день рождения или смерти.
# Например: 26th February 1802 - Victor Hugo's birthday - author of Les Misérables.

def read_file_txt(filename):
    list= []
    reg = r"\d{1,2}[a-z]{2}\s[A-Z][a-z]{2,8}\s\d{4}"
    reg2 = r"-.+\w+\b's"
    with open(filename, "r") as filetxt:
        for strings1 in filetxt.readlines():
            if (("birthday" in strings1.lower()) or ("death" in strings1.lower())) and re.findall(reg, strings1) and re.findall(reg2, strings1):
                list.append(strings1)
    return list

print(len(read_file_txt("authors.txt")), "readfile")



# 2.2) Написать функцию, которая принимает список строк полученной в пункте 2.1, и возвращает список словарей
# в формате {"name": name, "date": date},
# где name это имя автора, а date - дата из строки в формате "dd/mm/yyyy" (d-день, m-месяц, y-год)
#
# Например [{"name": "Charles Dickens", "date": "09/06/1870"}, ...,
# {"name": "J. D. Salinger", "date": "01/01/1919"}]

def get_day_from_string(string):
    dayin = r"\d{1,2}[a-z]{2}"
    if len(re.findall(dayin, string)[0][:-2]) == 1:
        return '0' + re.findall(dayin, string)[0][:-2]
    else:
        return re.findall(dayin, string)[0][:-2]


def get_year_fromstring(string):
    yearin = r"\d{4}"
    return re.findall(yearin,string)[0]

def change_month_name_to_number(string):
    month_in_year = {"January": "01",
                     "February": "02",
                     "March": "03",
                     "April": "04",
                     "May": "05",
                     "June": "06",
                     "July": "07",
                     "August": "08",
                     "September": "09",
                     "October": "10",
                     "November": "11",
                     "December": "12"}
    for month in month_in_year:
        if month in string:
            return month_in_year[month]

def create_dict_from_string(data):
    dict_list = []
    author_name = r"-.+\w+\b's"
    for string in data:
        dict_list.append({"name": (re.findall(author_name, string))[0][2:-2], "date": get_day_from_string(string) + "/" + change_month_name_to_number(string) + "/" + get_year_fromstring(string)})
    return dict_list


print(create_dict_from_string(read_file_txt("authors.txt")))


# 2.3) Написать функцию, которая сохраняет результат пункта 2.2 в json файл.

def write_json_file(data, filename="test2.json"):
    with open(filename, "w") as jsonfile:
        json.dump(data, jsonfile, ensure_ascii=False, indent=4)


write_json_file(create_dict_from_string(read_file_txt("authors.txt")))
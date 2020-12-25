# 1. Считать данные из файла domains.txt
# Названия интернет доменов поместить в список (названия сохранить без точки).

import random
import string

with open('domains', "r") as txt_file:
    domains = []
    for line in txt_file.readlines():
        domains.append(line.strip()[1:])
print(domains)

# 2. Считать данные из файла names.txt и поместить в список только фамилии из файла.
# Каждая строка файла содержит номер, фамилию, страну, некоторое число (таблица взята с википедии).
# Фамилия находится всегда на одной и той же позиции в строке.

with open('names', "r") as txt_file:
    names = []
    for line in txt_file.readlines():
        names.append(line.split()[1])

print(names)


# 3. Написать функцию для генерирования e-mail в формате:
# фамилия.число_от_100_до_999@строка_букв_длинной_от_5_до_7_символов.домен
# фамилию и домен брать из списков, полученных в задачах 1 и 2 и переданных в функцию в виде параметров.
# Строку и число генерировать случайным образом.
# Буквы в строке МОГУТ повторяться (перемешивание алфавита не подойдет, так как буквы не смогут повторяться)



def create_email(d_domains, n_names):
    surname = n_names[random.randint(0, len(n_names)-1)]
    result_numbers = random.randint(100, 999)
    result_str = ''.join(random.choice(string.ascii_lowercase) for i in range(random.randint(5, 7)))
    domain = d_domains[random.randint(0, len(d_domains)-1)]
    return surname.lower() + "." + str(result_numbers) + "@" + result_str + "." + domain

email = create_email(domains, names)
print(email)


#
# >>>miller.249@sgdyyur.com
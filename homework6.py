# 1. Дан список строк my_list. Создать новый список в который поместить
# элементы из my_list по следующему правилу:
# Если строка стоит на нечетном месте в my_list, то ее заменить на
# перевернутую строку. "qwe" на "ewq".
# Если на четном - оставить без изменения.
# Задание сделать с использованием enumerate.

my_list = ["1sfgh", "ddd1", "ewr", "czx", "jj234j", "kljbjkb"]

for index, value in enumerate(my_list):
    if index % 2:
        my_list[index] = value[::-1]

print(my_list)

########################################################################################################################

# 2. Дан список строк my_list. Создать новый список в который поместить
# элементы из my_list у которых первый символ - буква "a".

my_list = ["asdf", "eart", "aerf", "tygr", "awes"]
mynew_list = []
for index, value in enumerate(my_list):
    if value[0] =='a':
        mynew_list.append(value)
print(mynew_list)

########################################################################################################################

# 3. Дан список строк my_list. Создать новый список в который поместить
# элементы из my_list в которых есть символ - буква "a" на любом месте.

my_list = ["asdf", "eart", "aerf", "tygr", "awes"]
mynew_list = []
for value in my_list:
    if 'a' in value:
        mynew_list.append(value)
print(mynew_list)

########################################################################################################################

# 4. Дан список my_list в котором могум быть как строки (type str) так и целые числа (type int).
# Создать новый список в который поместить только строки из my_list.

my_list = ["qwer", 1123, 3132, "asdw", "dfgh"]
mynew_list = []
for value in my_list:
    if type(value) is str:
        mynew_list.append(value)
print(mynew_list)

########################################################################################################################

# 5. Дана строка my_str. Создать список в который поместить те символы из my_str,
# которые встречаются в строке только один раз.

my_str = "mlmdclksdckkdyuasdf"
my_list = []
for value in my_str:
    if my_str.count(value) == 1:
        my_list.append(value)
print(my_list)

########################################################################################################################

# 6. Даны две строки. Создать список в который поместить те символы,
# которые есть в обеих строках хотя бы раз.

my_str = 'msemlsdfl wkeosdpo'
my_str1 = 'qwqwqwqwqwr'

my_set = set(my_str+my_str1)
print(list(my_set))

########################################################################################################################

# 7. Даны две строки. Создать список в который поместить те символы, которые есть в обеих строках,
# но в каждой только по одному разу.

my_str = "qwe"
my_str2 = "qaрprrez"
new_list = []
for i in my_str and my_str2:
    if my_str.count(i) == 1:
        new_list.append(i)
        # print(set(new_list))
mylist = set(new_list)
print(mylist)

########################################################################################################################

# 8. Описать с помощью словаря следующую структуру для конкретного человека (можно придумать):
# Фамилия
# Имя
# Возраст
# Проживание
#     Страна
#     Город
#     Улица
# Работа
#     Наличие
#     Должность
my_dict = {"l_name": "Ivanov",
          "f_name": "Ivan",
          "age": 40,
          "address": {"country": "Ukraine",
                       "city": "Kyiv",
                       "street": "Nezalezhnosty"},
            "job": {"availability": "yes",
                     "position":"barber"}}
print(my_dict["age"])
print(my_dict["address"]["street"])


# 9. Описать с помощью словаря следующую структуру (рецепт ненастоящего торта,
# придумать и указать граммы для продуктов):

#Cоставляющие
#     Коржи
#         Мука
#         Молоко
#         Масло
#         Яйцо
#     Крем
#         Сахар
#         Масло
#         Ваниль
#         Сметана
#     Глазурь
#         Какао
#         Сахар
#         Масло

Sostav = {"Cakes": {"flour": 250,
                    "milk": 400,
                    "better": 120,
                    "egg": 2},
          "Cream": {"sugar": 300,
                    "better": 140,
                    "vanil": 2,
                    "sour_cream":80},
          "Glaze": {"cacao":230,
                    "sugar":300,
                    "oil":20}}
print(Sostav["Cakes"]["egg"])





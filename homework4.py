# 1) У вас есть список my_list с значениями типа int.
# Распечатать те значения, которые больше 100.
# Задание выполнить с помощью цикла for.

my_list = [98, 99, 100, 101, 102]
for symbol in my_list:
    if symbol > 100:
        print(symbol)
########################################################################################################################
# 2) У вас есть список my_list с значениями типа int, и пустой список my_results.
# Добавить в my_results те значения, которые больше 100.
# Распечатать список my_results.
# Задание выполнить с помощью цикла for.

my_list = [98, 99, 100, 101, 102]
my_results = []
for symbol in my_list:
    if symbol > 100:
        my_results.append(symbol)
print(my_results)

########################################################################################################################
# 3) У вас есть список my_list с значениями типа int.
# Если в my_list количество элементов меньше 2, то в конец добавить значение 0.
# Если количество элементов больше или равно 2, то добавить сумму последних двух элементов.
# Количество элементов в списке можно получить с помощью функции len(my_list)

my_list = [98, 99, 100, 101, 102]
results = my_list.append(0) if len(my_list) < 2 else my_list.append(my_list[-1] + my_list[-2])

print(my_list)

########################################################################################################################
# 4) Пользователь вводит value - число с запятой (например 3.14) с клавиатуры.
# Вы приводите это value к типу float и выводите результат выражения value ** -1.
# Написать программу, которая вычисляет данное выражение и
# корректно обрабатывает возможные исключения.

value = input('Введите число с запятой')
try:
    value = float(value)
    print(value ** -1)
except ValueError:
    print("Введите число в формате 3.14")
except ZeroDivisionError:
    print("0 нельзя возвести в отрицательную степень, введите число в формате 3.14 ")

########################################################################################################################
# Рассмотрим еще один пример использования списка -
# использование списка чисел для доступа по индексу к строке.
#
# my_indexes = [0, 1, 2, 3, 4]
# my_string = "abcde"
# for index in my_indexes:
# 	print(my_string[index]) # это называется обращение по индексу

########################################################################################################################
# 5) У вас есть список значений my_list и список индексов my_indexes
# (начинается с нуля и количество элементов совпадает с количеством в my_list.
# Распечатать значения из my_list через обращение по индексу. См. пример выше.

my_indexes = [0, 1, 2, 3, 4]
my_list = "abcde"
my_new_list = list(my_list)
for index in my_indexes:
	print(my_new_list[index])

########################################################################################################################
# 6) У вас есть два списка my_list_1 и my_list_2 равной длинны и
# список индексов my_indexes (начинается с нуля и количество элементов
# совпадает с количеством в my_list_1.
# Распечатать пары значений из my_list_1 и my_list_2 через обращение по индексу.
#
# Например для списков [1, 3] и [2, 4]:
# (1, 2)
# (3, 4)

my_list_1 = [11, 22, 33, 44, 55]
my_list_2 = [5, 4, 3, 2, 1]
my_indexes = [0, 1, 2, 3, 4]
for index in my_indexes:
	print(my_list_1[index], my_list_2[index])

########################################################################################################################
# Еще один пример - вложенные циклы (цикл в цикле).
# my_string_1 = "12"
# my_string_2 = "34"
# for symb_1 in my_string_1:
# 	for symb_2 in my_string_2:
# 		print(symb_1 + symb_2)
#
# Результат:
# "13"	# перебирается все элементы из my_string_2 для элемента "1" из my_string_1
# "14"
# "23"	# перебирается все элементы из my_string_2 для элемента "2" из my_string_1
# "24"

########################################################################################################################

# 7) У вас есть строка my_string = '0123456789'.
# Сгенерировать целые числа (тип int) от 0 до 99 и поместить их в список.
# Задание нужно выполнить ТОЛЬКО через цикл в цикле(См. пример выше) и приведение типов .
# Генерирование через range или другие "фишки" я засчитывать не буду ))


my_string = "0123456789"
my_list = []
for symb_1 in my_string:
	for symb_2 in my_string:
		my_list.append(int(symb_1 + symb_2))
print (my_list)

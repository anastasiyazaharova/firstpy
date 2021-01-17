# # Щелчек Таноса
# # 1. Создать папку ./alphabet/ или проверить, что папка существует.
# import os
# from os.path import join as p_join
# from os.path import isfile
# from string import ascii_lowercase as alphabet
#
# def tanos_click(dirname):
#     files = sorted(file for file in os.listdir(dirname) if os.path.isfile(p_join(dirname, file)))
#     for file in list(set(files))[:len(files)//2]:
#         os.remove(p_join(dirname, file))
#
#
# def create_txt_files(dirname):
#     for i in alphabet:
#         file_name = os.path.join(dirname, f'{i}.txt')
#         write_txt_file(file_name,alphabet.replace(i, i.upper()))
#
# def write_txt_file(filename, data):
#     with open(filename, "w") as txt_file:
#         txt_file.write(data)
#
#
#
# def create_dir(dir_name):
#     try:
#         os.mkdir(dir_name)
#     except FileExistsError:
#         pass
#
#
# dir_name = 'alpahabet'
# # create_dir(dir_name)
# # create_txt_files(dir_name)
# tanos_click(dir_name)
#
# # 2. В папку ./alphabet/ поместить файлы вида a.txt, b.txt, ..., z.txt в которых
# # будет записана строка алфавита, но с заменой буквы из названия файла на прописную.
# # Пример: для b.txt строка будет aBcde...
# # 3. Сделать щелчек Таноса - удалить случайным образом половину всех файлов в этой папке.

[0-9]  #цифра
[]
import re

# def key_sorted_by_age(obj_dict):
#     age = obj_dict["age"]
#     return age
def key_sorted_by_name(obj_dict):
    return obj_dict["name"]

def key_sorted_by_len(obj_dict):
    return len(obj_dict["name"])

dict_list = [
    {"name": "Jonh", "age": "1900 - 1989"},
    {"name": "Zoy", "age": "1878 - 1899"},
    {"name": "Sonya", "age": "1901 - 1978"}
]

def key_sorted_by_age(obj_dict):
    ages = re.findall(r'\d+', obj_dict["age"])
    d_data = ages[-1]
    return int(d_data)


new_dict_list = sorted(dict_list, key=key_sorted_by_age)
test_list = ['asd', "poi", "ju", "i", "787"]
new_test_list = sorted(test_list, key=len)
numb_list = [1,2,3,-34,-2,0,10,-134]
new_numb_test = sorted(numb_list)

print(new_test_list)
print(new_numb_test)
print(new_dict_list)
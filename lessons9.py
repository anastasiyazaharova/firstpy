import json
import csv
#
# # with open("txt.json", 'r', encoding='utf-8') as json_file:
# #     data = json.load(json_file)
# #
# # print(data)
# # print(type(data))
# #
# # data ["last_name"] = "Connor"
# # data_txt = json.dumps(data)
# # # data_txt_2 = str(data)
# # # print(data_txt)
# # # print(data_txt_2)
# #
# # with open("test_new.json", 'w') as json_file:
# #     j, json_file, indent=4)son.dump(data
#
# with open("extensions.csv", 'r', encoding='utf-8') as csv_file:
#     data = []
# #     reader = csv.DictReader(csv_file)
# #     for row in reader:
# #         data.append(row)
# #
# # print(data)
# # for row in data:
# #     print('email:', row["name"])
#
#     reader = csv.reader(csv_file)
#     for row in reader:
#         data.append(row)
#
# data.append("рроророо". 45])
# with open ()
# # headers = data.pop(0)
# # print(data)
# # print(headers)

def read_txt(filename):
    with open(filename, 'r') as file:
        data = []
        for line in file.readlines():
            data.append(line.strip())
    return data

def read_json(filename):
    with open(filename, 'r', encoding='utf=8')  as json_file:
        data = json.load(json_file)
    return data

def read_csv(filename):
    with open(filename, 'r') as csv_file:
        data = []
        reader = csv.DictReader(csv_file)
        for row in reader:
            data.append(row)
    return data

def read_file(filename):
    ext = filename.split(".")[-1]
    if ext == 'txt':
        result = read_txt(filename)
    elif ext == "json":
        result = read_json(filename)
    elif ext == "csv":
        result = read_csv(filename)
    else:
        print = ('IncorrectFileType')
        result = ''
    return result


result_txt = read_file("forl8.txt.txt")
print(result_txt)
result_json = read_file("txt.json")
print(result_json)
result_csv = read_file("extensions.csv")
print(result_csv)
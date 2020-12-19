import _json
import csv
def read_txt(filename):
    with open(filename, 'r') as file:
        data = []
    for




def read_file(filename):
    ext = filename.split(".") [-1]
    if ext == 'txt':
        result = read_txt(filename)
    elif ext == 'json':
        result = read_json(filename)
    elif ext == 'csv':
        result = read_csv(filename)
    else:
        print('IncorectFileType')

    return filename

result_txt = read_file("firstpy/test.txt")
result_json = read_file("test.json")
result_csv = read_file('test.csv')
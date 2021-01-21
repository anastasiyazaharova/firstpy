# # import re
# #
# # test_str = 'My e-mail is anastasiyazaharova1@gmail.com and IP 123.23.456.1 and 1111111.123.32.233'
# #
# # reg_exp = r'\w+@\w+\.\w+'
# #
# # reg_exp = r'\b\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\b'
# #
# # result = re.findall(reg_exp, test_str)
# # print(result)
# #
# # result_1 = (lambda x: x + 3)(4)
#
# data = [2, 63, 7, 8, 196, 6, 99]
# print([n for n in data if n % 2])
#
# def fil_fun(n):
#     return n % 2
#
# print(list(filter(fil_fun, data)))

# print(list(filter(lambda x: x % 2, data)))

# from urllib .request import Request
import requests

url = "http://api.forismatic.com/api/1.0/"

params = {"method": "getQuote",
          "format": "json",
          "key": 1,
          "lang": "ru"}
for i in range(10):
    params["key"] = i
    r = requests.get(url, params=params)
    quote = r.json()
    # print(quote)
    quote_text = quote["quoteText"]
    print(quote_text)
    quote_author = quote["quoteAuthor"]
    print(quote_author)







# res = requests.get(url)
# print(res)
# with url
# res = Request(url)
#
# print(res.h)



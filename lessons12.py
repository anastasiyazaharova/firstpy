import re

test_str = 'My e-mail is anastasiyazaharova1@gmail.com and IP 123.23.456.1 and 1111111.123.32.233'

reg_exp = r'\w+@\w+\.\w+'

reg_exp = r'\b\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\b'

result = re.findall(reg_exp, test_str)
print(result)

result_1 = (lambda x: x + 3)(4)


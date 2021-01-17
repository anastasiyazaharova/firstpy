# # points = {"A": {(0,0),
# #           "B": (2,4)}
# # print(points['B'][0])
#
# class Point:
#     x = 0
#     y = 0
#
# # point_A = Point()
# # B = Point()
# # B.x = 2
# # B.y = 4
# # print(point)
#
# class Person:
#     # name = "Jon"
#     # age = 20
#     # job = "slesar"
#     # address = 'Street, House'
#
#     def __init__(self, name, age, job, address):
#         self.name = name
#         self.age = age
#         self.job = job
#         self.address = address
#
#     def increase_age(self):
#         self.age +=1
#
# person_1 = Person("John", 20, "slesar", 'Street')
# person_1.increase_age()
#
# print(person_1.age)
# Person.family = '5'
# print(person_1.family)
# print(person_1.name)
# person_2 = Person("Maria", 30, "kok", 'Domik')
# print(person_2.name)
# print(person_2.family)


class Person:
    name= 'Cibuliya'
    age = 3

print(getattr(Person,'name'))
print(getattr(Person, 'x', 100))
print(getattr(Person, 'name', 100))

Person.x = 200
print(Person.__dict__)
delattr(Person, 'x')
print(Person.__dict__)




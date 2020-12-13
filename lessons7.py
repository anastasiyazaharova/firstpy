#libriary
import random
def create_random_point():
    point = (random.randint(-10, 10),
             random.randint(-10, 10),
             random.randint(-10, 10))
    return point
def create_line_segment():
    line_segment = {"A": create_random_point(),
                    "B": create_random_point()}
    return line_segment
def print_line_segment(line_segment):
    print(f'Отрезок AB: {line_segment["A"]}", {line_segment["B"]}')

# number = rnd.randint(1,10)
# from random import randint
# print(number)
#
AB = create_line_segment()
print_line_segment(AB)


from random import randrange
from math import gcd


RULES = 'Find the greatest common divisor of given numbers.'


def generate_question():
    num_1 = randrange(0, 1000, 5)
    num_2 = randrange(0, 1000, 5)
    return str(num_1) + ' ' + str(num_2)


def get_correct_answer(item):
    result = item.split()
    return gcd(int(result[0]), int(result[1]))

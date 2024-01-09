from random import randrange
from math import gcd


rules = 'Find the greatest common divisor of given numbers.'


def generates_question():
    result = []
    for i in range(3):
        num_1 = randrange(0, 1000, 5)
        num_2 = randrange(0, 1000, 5)
        result.append(str(num_1) + ' ' + str(num_2))
    return result


def correct_answer(items):
    result = []
    for i in items:
        item = i.split()
        result.append(gcd(int(item[0]), int(item[1])))
    return result


question = generates_question()

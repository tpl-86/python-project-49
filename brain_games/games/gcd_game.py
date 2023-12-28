from random import randrange
from math import gcd


def rules():
    print('Find the greatest common divisor of given numbers.')


def num_1():
    number = randrange(0, 1000, 5)
    return number


def num_2():
    number = randrange(0, 1000, 5)
    return number


def quastion(num_1, num_2):
    return f"{num_1} {num_2}"


def correct_answer(num_1, num_2):
    result = gcd(num_1, num_2)
    return result

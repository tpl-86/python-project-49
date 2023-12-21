from random import randint


def value():
    return randint(1, 100)


def result(number):
    if number % 2 == 0:
        return 'yes'
    else:
        return 'no'

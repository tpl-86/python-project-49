import random


def rules():
    print('Answer "yes" if given number is prime. Otherwise answer "no".')


def quastion():
    number = random.randint(0, 1000)
    return number


def correct_answer(number):
    for i in range(2, (number // 2) + 1):
        if number % i == 0:
            return 'no'
    return 'yes'

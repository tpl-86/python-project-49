from random import randint


def rules():
    print('Answer "yes" if the number is even, otherwise answer "no".')

def quastion():
    value = randint(1, 100)
    return value

def correct_answer(number):
    if number % 2 == 0:
        return 'yes'
    else:
        return 'no'

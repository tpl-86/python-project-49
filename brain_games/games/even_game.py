from random import randint


RULES = 'Answer "yes" if the number is even, otherwise answer "no".'


def generate_question():
    result = randint(1, 100)
    return result


def is_even(num):
    if num % 2 == 0:
        return True
    else:
        return False


def get_correct_answer(item):
    if is_even(item):
        return 'yes'
    else:
        return 'no'

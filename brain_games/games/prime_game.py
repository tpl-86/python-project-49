from random import randint


RULES = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def generate_question():
    num = randint(0, 1000)
    return num


def is_prime(item):
    if item < 2:
        return False
    for i in range(2, (item // 2) + 1):
        if item % i == 0:
            return False
    return True


def get_correct_answer(item):
    if is_prime(item):
        return 'yes'
    else:
        return 'no'

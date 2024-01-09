from random import randint


rules = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def generates_question():
    result = []
    for i in range(3):
        number = randint(0, 1000)
        result.append(number)
    return result


def is_prime(item):
    for i in range(2, (item // 2) + 1):
        if item % i == 0:
            return 'no'
    return 'yes'


def correct_answer(items):
    result = []
    for item in items:
        result.append(is_prime(item))
    return result


question = generates_question()

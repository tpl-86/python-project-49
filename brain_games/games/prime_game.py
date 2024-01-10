from random import randint


rules = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def generate_question():
    result = []
    for i in range(3):
        num = randint(0, 1000)
        result.append(num)
    return result


def is_prime(item):
    if item < 2:
        return 'no'
    for i in range(2, (item // 2) + 1):
        if item % i == 0:
            return 'no'
    return 'yes'


def get_correct_answer(items):
    result = []
    for item in items:
        result.append(is_prime(item))
    return result


question = generate_question()

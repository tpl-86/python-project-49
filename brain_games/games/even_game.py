from random import randint


RULES = 'Answer "yes" if the number is even, otherwise answer "no".'


def generate_question():
    result = []
    for i in range(3):
        num = randint(1, 100)
        result.append(num)
    return result


def get_correct_answer(items):
    result = []
    for i in items:
        if i % 2 == 0:
            result.append('yes')
        else:
            result.append('no')
    return result


question = generate_question()

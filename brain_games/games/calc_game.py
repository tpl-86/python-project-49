from random import randint, choice


RULES = 'What is the result of the expression?'


def generate_question():
    operation = '+-*'
    a = randint(1, 100)
    b = randint(1, 100)
    sign = choice(operation)
    result = str(a) + ' ' + sign + ' ' + str(b)
    return result


def get_correct_answer(item):
    list_substrings = item.split()
    if '*' in list_substrings:
        return int(list_substrings[0]) * int(list_substrings[2])
    elif '+' in list_substrings:
        return int(list_substrings[0]) + int(list_substrings[2])
    else:
        return int(list_substrings[0]) - int(list_substrings[2])

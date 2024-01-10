from random import randint, choice


RULES = 'What is the result of the expression?'


def generate_question():
    result = []
    operation = '+-*'
    for i in range(3):
        a = randint(1, 100)
        b = randint(1, 100)
        sign = choice(operation)
        result.append(str(a) + ' ' + sign + ' ' + str(b))
    return result


def get_correct_answer(items):
    result = []
    for i in items:
        if '*' in i:
            list_substrings = i.split()
            result.append(int(list_substrings[0]) * int(list_substrings[2]))
        elif '+' in i:
            list_substrings = i.split()
            result.append(int(list_substrings[0]) + int(list_substrings[2]))
        else:
            list_substrings = i.split()
            result.append(int(list_substrings[0]) - int(list_substrings[2]))
    return result


question = generate_question()

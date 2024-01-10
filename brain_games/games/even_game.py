from random import randint


rules = "Answer 'yes' if the number is even, otherwise answer 'no'."


def generates_question():
    result = []
    for i in range(3):
        value = randint(1, 100)
        result.append(value)
    return result


def correct_answer(items):
    result = []
    for i in items:
        if i % 2 == 0:
            result.append('yes')
        else:
            result.append('no')
    return result


question = generates_question()

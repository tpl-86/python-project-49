import random


def rules():
    print('What number is missing in the progression?')


def progression_output():
    start = random.randint(0, 100)
    step = random.randint(1, 11)
    progression_length = random.randint(5, 10)
    result = []
    for i in range(progression_length):
        result.append(start + i * step)
    return result


def quastion(progression, item):
    result = ''
    for i in range(len(progression)):
        if progression[i] == item:
            result += '..' + ' '
        else:
            result += str(progression[i]) + ' '
    return result


def correct_answer(progression):
    item = random.randrange(0, len(progression) - 1)
    result = progression[item]
    return result

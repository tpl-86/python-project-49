import random


RULES = 'What number is missing in the progression?'


def generate_progression():
    result = []
    start = random.randint(0, 100)
    step = random.randint(1, 11)
    progression_length = random.randint(5, 10)
    for i in range(progression_length):
        result.append(start + i * step)
    return result


def generate_question():
    progression = generate_progression()
    result = ''
    random_value = random.randrange(len(progression))
    item = progression[random_value]
    for i in progression:
        if i == item:
            result += '..' + ' '
        else:
            result += str(i) + ' '
    return result


def get_correct_answer(string):
    list_of_string = string.split()
    if list_of_string[0] == '..':
        value = int(list_of_string[2]) - int(list_of_string[1])
        result = int(list_of_string[1]) - value
        return result
    elif list_of_string[-1] == '..':
        value = int(list_of_string[2]) - int(list_of_string[1])
        result = int(list_of_string[-2]) + value
        return result
    for i in range(len(list_of_string)):
        if list_of_string[i] == '..':
            d = (int(list_of_string[-1]) - int(list_of_string[0])) / \
                (len(list_of_string) - 1)
            result = int(list_of_string[i - 1]) + int(d)
            return result

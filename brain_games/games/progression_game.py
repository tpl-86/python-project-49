import random


rules = 'What number is missing in the progression?'


def progression_output():
    result = []
    for i in range(3):
        start = random.randint(0, 100)
        step = random.randint(1, 11)
        progression_length = random.randint(5, 10)
        result_progression = []
        for j in range(progression_length):
            result_progression.append(start + j * step)
        result.append(result_progression)
    return result


def generates_quastions(list_progressions, items):
    result = []
    for i in range(len(list_progressions)):
        result_progression = ''
        for j in range(len(list_progressions[i])):
            if list_progressions[i][j] == items[i]:
                result_progression += '..' + ' '
            else:
                result_progression += str(list_progressions[i][j]) + ' '
        result.append(result_progression)
    return result


def correct_answer(list_progressions):
    result = []
    for progression in list_progressions:
        item = random.randrange(0, len(progression) - 1)
        result.append(progression[item])
    return result


progressions = progression_output()
answers = correct_answer(progressions)
quastions = generates_quastions(progressions, answers)

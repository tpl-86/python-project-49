from random import randint, choice


def rules():
    print('What is the result of the expression?')


def number_1():
    number = randint(1, 50)
    return number


def number_2():
    number = randint(1, 50)
    return number


def sign():
    operation = '+-*'
    result = choice(operation)
    return result


def quastion(num_1, sign, num_2):
    return str(num_1) + sign + str(num_2)


def correct_answer(operand_1, sign, operand_2):
    if sign == '*':
        result = operand_1 * operand_2
        return result
    elif sign == '+':
        result = operand_1 + operand_2
        return result
    else:
        result = operand_1 - operand_2
        return result

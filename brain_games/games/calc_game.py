from random import rendint, choice


def value():
    num_1 = randint(1, 20)
    num_2 = randint(1, 20)
    operation = '+-*'
    sign = choice(operation)
    return str(num_1) sign str(num_2)


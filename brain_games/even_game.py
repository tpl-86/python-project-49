import prompt
from random import randint


def even_number():
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}')
    print('Answer "yes" if the number is even, '
          'otherwise answer "no".')
    for i in range(3):
        number = randint(1, 100)
        print('Quastion: ', number)
        answer = prompt.string('Your answer: ')
        if number % 2 == 0:
            if answer == 'yes':
                print('Correct!')
            else:
                return print(f"'{answer}' is wrong "
                             "answer ;(. Correct answer was 'yes'.")
        else:
            if answer == 'no':
                print('Correct!')
            else:
                return print(f"'{answer}' is wrong "
                             "answer ;(. Correct answer was 'no'.")
    return print(f'Congratulations, {name}!')

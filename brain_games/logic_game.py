import prompt


def welcome_user():
    name = prompt.string('May I have yuor name? ')
    print(f'Hello, {name}!')
    return name


def play_game(quastion, correct_answer):
    print('Quastion: ', quastion)
    answer = prompt.string('Your answer: ')
    if answer == correct_answer:
        return 'Correct!'
    else:
        return f"'{answer}' is wrong answer ;(. \
                Correct answer was '{correct_answer}'."

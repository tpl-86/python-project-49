import prompt


def welcome_user():
    name = prompt.string('May I have yuor name? ')
    print(f'Hello, {name}!')
    return name


def play_game(rules, quastion, correct_answer):
    name = prompt.string('May I have yuor name? ')
    print(f'Hello, {name}!')
    print(rules)
    for i in range(3):
        print('Quastion: ', quastion[i])
        answer = prompt.string('Your answer: ')
        if answer == str(correct_answer[i]):
            print('Correct!')
        else:
            return (f"'{answer}' is wrong answer ;(. "
                    f"Correct answer was '{correct_answer[i]}'."
                    f"\nLet's try again, {name}!")
    return (f'Congratulations, {name}!')

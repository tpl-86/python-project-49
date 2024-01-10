import prompt


def play_game(rules, question, correct_answer):
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print(rules)
    for i in range(3):
        print('Question:', question[i])
        answer = prompt.string('Your answer: ')
        if answer == str(correct_answer[i]):
            print('Correct!')
        else:
            return (f"'{answer}' is wrong answer ;(. "
                    f"Correct answer was '{correct_answer[i]}'."
                    f"\nLet's try again, {name}!")
    return (f'Congratulations, {name}!')

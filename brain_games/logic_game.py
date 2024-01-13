import prompt


def play_game(game):
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print(game.RULES)
    for i in range(3):
        question = game.generate_question()
        print('Question:', question)
        answer = prompt.string('Your answer: ')
        if answer == str(game.get_correct_answer(question)):
            print('Correct!')
        else:
            return (f"'{answer}' is wrong answer ;(. "
                    f"Correct answer was '{game.get_correct_answer(question)}'."
                    f"\nLet's try again, {name}!")
    return (f'Congratulations, {name}!')

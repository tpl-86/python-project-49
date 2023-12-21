import prompt
from brain_games.games import even_game


def play_game():
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    for i in range(3):
        quastion = even_game.value()
        correct_answer = even_game.result(quastion)
        print('Quastion, ', quastion)
        answer = prompt.string('Your answer: ')
        if answer == correct_answer:
            print('Correct!')
        else:
            return print(f"'{answer}' is wrong answer ;(."
                         f"Correct answer was '{correct_answer}'")
    print(f'Congratulations, {name}!')

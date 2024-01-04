#!/usr/bin/env python3

from brain_games import logic_game
from brain_games.games import prime_game


def greet():
    print('Welcome to the Brain Games!')


def main():
    greet()
    user_name = logic_game.welcome_user()
    prime_game.rules()
    for i in range(3):
        quastion_game = prime_game.quastion()
        answer_game = prime_game.correct_answer(quastion_game)
        result = logic_game.play_game(quastion_game, answer_game)
        if result == 'Correct!':
            print(result)
        else:
            return result + f"\nLet's try again, {user_name}!"
    print(f'Congratulations, {user_name}!')


if __name__ == '__main__':
    main()

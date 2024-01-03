#!/usr/bin/env python3

from brain_games import logic_game
from brain_games.games import progression_game


def greet():
    print('Welcome to the Brain Games!')


def main():
    greet()
    user_name = logic_game.welcome_user()
    progression_game.rules()
    for i in range(3):
        progression = progression_game.progression_output()
        answer_game = progression_game.correct_answer(
            progression)
        quastion_game = progression_game.quastion(
            progression, answer_game)
        result = logic_game.play_game(quastion_game, answer_game)
        if result == 'Correct!':
            print(result)
        else:
            return result + f"\nLet's try again, {user_name}!"
    print(f'Congratulations, {user_name}!')


if __name__ == '__main__':
    main()

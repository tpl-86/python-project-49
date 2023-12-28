#!/usr/bin/env python3

from brain_games import logic_game
from brain_games.games import gcd_game


def greet():
    print('Welcome to the Brain Games!')


def main():
    greet()
    user_name = logic_game.welcome_user()
    gcd_game.rules()
    for i in range(3):
        number_1 = gcd_game.num_1()
        number_2 = gcd_game.num_2()
        quastion_game = gcd_game.quastion(
            number_1, number_2)
        answer_game = gcd_game.correct_answer(
            number_1, number_2)
        result = logic_game.play_game(quastion_game, answer_game)
        if result == 'Correct!':
            print(result)
        else:
            return result + f"\nLet's try again, {user_name}!"
    print(f'Congratulations, {user_name}!')


if __name__ == '__main__':
    main()

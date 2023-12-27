#!/usr/bin/env python3

from brain_games import logic_game
from brain_games.games import calc_game


def greet():
    print('Welcome to the Brain Games!')


def main():
    greet()
    user_name = logic_game.welcome_user()
    calc_game.rules()
    for i in range(3):
        operand_1 = calc_game.number_1()
        operand_2 = calc_game.number_2()
        sign_expression = calc_game.sign()
        quastion_game = calc_game.quastion(
            operand_1, sign_expression, operand_2,
        )
        answer_game = calc_game.correct_answer(
            operand_1, sign_expression, operand_2,
        )
        result = logic_game.play_game(quastion_game, str(answer_game))
        if result == 'Correct!':
            print(result)
        else:
            return result + f"\nLet's try again, {user_name}!"
    print(f'Congratulations, {user_name}!')


if __name__ == '__main__':
    main()

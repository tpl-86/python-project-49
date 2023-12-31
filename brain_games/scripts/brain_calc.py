#!/usr/bin/env python3

from brain_games import logic_game
from brain_games.games import calc_game


def greet():
    print('Welcome to the Brain Games!')


def main():
    greet()
    return logic_game.play_game(calc_game.rules,
                                calc_game.quastion,
                                calc_game.correct_answer(calc_game.quastion))


if __name__ == '__main__':
    main()

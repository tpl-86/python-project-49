#!/usr/bin/env python3

from brain_games import logic_game
from brain_games.games import calc_game


def main():
    return logic_game.play_game(calc_game.rules,
                                calc_game.question,
                                calc_game.correct_answer(calc_game.question))


if __name__ == '__main__':
    main()

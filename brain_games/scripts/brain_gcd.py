#!/usr/bin/env python3

from brain_games import logic_game
from brain_games.games import gcd_game


def main():
    return logic_game.play_game(gcd_game.rules,
                                gcd_game.question,
                                gcd_game.correct_answer(gcd_game.question))


if __name__ == '__main__':
    main()

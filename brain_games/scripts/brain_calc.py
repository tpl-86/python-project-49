#!/usr/bin/env python3

from brain_games import logic_game
from brain_games.games.calc_game import RULES, question, get_correct_answer


def main():
    print(logic_game.play_game(RULES,
                               question,
                               get_correct_answer(question)))


if __name__ == '__main__':
    main()

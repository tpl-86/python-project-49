#!/usr/bin/env python3

from brain_games.logic_game import play_game
from brain_games.games.gcd_game import RULES, question, get_correct_answer


def main():
    print(play_game(RULES,
                    question,
                    get_correct_answer(question)))


if __name__ == '__main__':
    main()

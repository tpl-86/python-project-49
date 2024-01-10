#!/usr/bin/env python3

from brain_games.logic_game import play_game
from brain_games.games.progression_game import RULES, question, answer


def main():
    print(play_game(RULES,
                    question,
                    answer))


if __name__ == '__main__':
    main()

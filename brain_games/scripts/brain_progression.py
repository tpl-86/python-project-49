#!/usr/bin/env python3

from brain_games.logic_game import play_game
from brain_games.games.progression_game import rules, question, answer


def main():
    print(play_game(rules,
                    question,
                    answer))


if __name__ == '__main__':
    main()

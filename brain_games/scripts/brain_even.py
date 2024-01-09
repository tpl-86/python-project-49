#!/usr/bin/env python3

from brain_games import logic_game
from brain_games.games.even_game import rules, quastion, correct_answer


def greet():
    print('Welcome to the Brain Games!')


def main():
    greet()
    return logic_game.play_game(rules, quastion, correct_answer(quastion))


if __name__ == '__main__':
    main()

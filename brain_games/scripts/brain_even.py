#!/usr/bin/env python3

from brain_games import logic_game
from brain_games.games import even_game


def greet():
    print('Welcome to the Brain Games!')


def main():
    greet()
    return logic_game.play_game(even_game.rules,
                                even_game.question,
                                even_game.correct_answer(even_game.question))


if __name__ == '__main__':
    main()

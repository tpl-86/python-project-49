#!/usr/bin/env python3

from brain_games import logic_game
from brain_games.games import prime_game


def greet():
    print('Welcome to the Brain Games!')


def main():
    greet()
    return logic_game.play_game(prime_game.rules,
                                prime_game.quastion,
                                prime_game.correct_answer(prime_game.quastion))


if __name__ == '__main__':
    main()

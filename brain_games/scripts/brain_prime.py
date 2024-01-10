#!/usr/bin/env python3

from brain_games import logic_game
from brain_games.games import prime_game


def main():
    print(logic_game.play_game(prime_game.rules,
                               prime_game.question,
                               prime_game.correct_answer(prime_game.question)))


if __name__ == '__main__':
    main()

#!/usr/bin/env python3

from brain_games import logic_game
from brain_games.games import even_game


def main():
    result = logic_game.play_game(even_game.rules,
                                  even_game.question,
                                  even_game.correct_answer(even_game.question))
    return result


if __name__ == '__main__':
    main()

#!/usr/bin/env python3

from brain_games import logic_game
from brain_games.games import progression_game


def main():
    print(logic_game.play_game(progression_game.rules,
                               progression_game.question,
                               progression_game.answer))


if __name__ == '__main__':
    main()

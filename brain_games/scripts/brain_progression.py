#!/usr/bin/env python3

from brain_games.logic_game import play_game
from brain_games.games import progression_game


def main():
    print(play_game(progression_game))


if __name__ == '__main__':
    main()

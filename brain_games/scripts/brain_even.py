#!/usr/bin/env python3

from brain_games import logic_game


def greet():
    print('Welcome to the Brain Games!')


def main():
    greet()
    logic_game.play_game()


if __name__ == '__main__':
    main()

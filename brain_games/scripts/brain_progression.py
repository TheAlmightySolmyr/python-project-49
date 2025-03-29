#!/usr/bin/env python


from brain_games.engine import run_game
from brain_games.games.progression_mod import PROGRESSION_RULES, get_progression


def main():
    run_game(get_progression, PROGRESSION_RULES)


if __name__ == '__main__':
    main()
#!/usr/bin/env python


from brain_games.engine import run_game
from brain_games.games.gcd_mod import GCD_RULES, get_gcd


def main():
    run_game(get_gcd, GCD_RULES)


if __name__ == '__main__':
    main()
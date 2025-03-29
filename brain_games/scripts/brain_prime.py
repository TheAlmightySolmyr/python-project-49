#!/usr/bin/env python


from brain_games.engine import run_game
from brain_games.games.prime_mod import PRIME_RULES, get_prime


def main():
    run_game(get_prime, PRIME_RULES)


if __name__ == '__main__':
    main()
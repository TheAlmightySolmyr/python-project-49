from brain_games.engine import run_game
from brain_games.games.prime_mod import get_prime


def main():
    run_game(get_prime)


if __name__ == '__main__':
    main()
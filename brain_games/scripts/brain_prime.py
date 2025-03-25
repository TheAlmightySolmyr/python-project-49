from brain_games.engine import run_three_time
from brain_games.games.prime_mod import get_prime


def main():
    run_three_time(get_prime)


if __name__ == '__main__':
    main()
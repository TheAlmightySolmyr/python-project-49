from brain_games.cli import run_three_time
from brain_games.games.prime_mod import prime_game


def main():
    run_three_time(prime_game)


if __name__ == '__main__':
    main()
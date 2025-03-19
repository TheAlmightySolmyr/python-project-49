from brain_games.cli import run_three_time
from brain_games.games.gcd_mod import gcd_game


def main():
    run_three_time(gcd_game)


if __name__ == '__main__':
    main()
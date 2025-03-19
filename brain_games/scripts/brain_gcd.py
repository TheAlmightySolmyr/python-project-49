from brain_games.cli import run_three_time
from brain_games.games.gcd_mod import get_gcd


def main():
    run_three_time(get_gcd)


if __name__ == '__main__':
    main()
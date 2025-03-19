from brain_games.cli import run_three_time
from brain_games.games.calc_mod import calc_game


def main():
    run_three_time(calc_game)


if __name__ == '__main__':
    main()
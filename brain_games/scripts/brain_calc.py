from brain_games.engine import run_three_time
from brain_games.games.calc_mod import get_calc


def main():
    run_three_time(get_calc)


if __name__ == '__main__':
    main()
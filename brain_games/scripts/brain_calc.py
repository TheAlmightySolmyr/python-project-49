from brain_games.engine import run_game
from brain_games.games.calc_mod import get_calc


def main():
    run_game(get_calc)


if __name__ == '__main__':
    main()
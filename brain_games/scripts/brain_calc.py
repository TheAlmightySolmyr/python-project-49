from brain_games.engine import run_game
from brain_games.games.calc_mod import CALC_RULES, get_calc


def main():
    run_game(get_calc, CALC_RULES)


if __name__ == '__main__':
    main()
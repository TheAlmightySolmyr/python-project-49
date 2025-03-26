from brain_games.engine import run_game
from brain_games.games.even_mod import EVEN_RULES, get_even


def main():
    run_game(get_even, EVEN_RULES)


if __name__ == '__main__':
    main()

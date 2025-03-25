from brain_games.engine import run_game
from brain_games.games.gcd_mod import get_gcd


def main():
    run_game(get_gcd)


if __name__ == '__main__':
    main()
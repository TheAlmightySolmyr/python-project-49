from brain_games.engine import run_three_time
from brain_games.games.even_mod import get_even


def main():
    run_three_time(get_even)


if __name__ == '__main__':
    main()

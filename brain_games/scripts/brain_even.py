from brain_games.cli import run_three_time
from brain_games.games.even_mod import even_game


def main():
    run_three_time(even_game)


if __name__ == '__main__':
    main()

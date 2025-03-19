from brain_games.cli import run_three_time
from brain_games.games.progression_mod import progression_game


def main():
    run_three_time(progression_game)


if __name__ == '__main__':
    main()
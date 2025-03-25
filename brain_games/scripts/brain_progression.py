from brain_games.engine import run_three_time
from brain_games.games.progression_mod import get_progression


def main():
    run_three_time(get_progression)


if __name__ == '__main__':
    main()
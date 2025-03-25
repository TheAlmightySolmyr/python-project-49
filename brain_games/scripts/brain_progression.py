from brain_games.engine import run_game
from brain_games.games.progression_mod import get_progression


def main():
    run_game(get_progression)


if __name__ == '__main__':
    main()
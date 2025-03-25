import random

from brain_games.engine import MAX_GEN_NUMBER, MIN_GEN_NUMBER


def is_even(num: int):
    return num % 2 == 0


def get_even():
    print('Answer "yes" if the number is even, otherwise answer "no".')
    question = random.randint(MIN_GEN_NUMBER, MAX_GEN_NUMBER)
    right_answer = 'yes' if is_even(question) else 'no'
    return question, right_answer
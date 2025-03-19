import random

import prompt

from brain_games.cli import is_right
from brain_games.engine import MAX_GEN_NUMBER, MIN_GEN_NUMBER


def is_even(num: int):
    return num % 2 == 0


def get_even():
    print('Answer "yes" if the number is even, otherwise answer "no".')
    question_num = random.randint(MIN_GEN_NUMBER, MAX_GEN_NUMBER)
    print(f'Question: {question_num}')
    answ = prompt.string('Your answer:')
    right_answ = 'yes' if is_even(question_num) else 'no'
    return is_right(answ, right_answ)
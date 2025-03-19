import random

import prompt

from brain_games.cli import is_right


def is_even(num: int):
    return num % 2 == 0


def even_game():
    print('Answer "yes" if the number is even, otherwise answer "no".')
    question_num = random.randint(1, 99)
    print(f'Question: {question_num}')
    answ = prompt.string('Your answer:')
    right_answ = 'yes' if is_even(question_num) else 'no'
    return is_right(answ, right_answ)
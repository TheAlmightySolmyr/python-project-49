import random

import prompt

from brain_games.cli import is_right

from brain_games.engine import MIN_GEN_NUMBER, MAX_GEN_NUMBER


def get_progression():
    start = random.randint(MIN_GEN_NUMBER, MAX_GEN_NUMBER)
    step = random.randint(MIN_GEN_NUMBER, MAX_GEN_NUMBER)
    rand_list = [start + i * step for i in range(10)]
    rand_index = random.randint(0, len(rand_list) - 1)
    question = rand_list[rand_index]
    rand_list[rand_index] = '..'
    print('What number is missing in the progression?')
    str_rand_list = [str(i) for i in rand_list]
    print(f'Question: {' '.join(str_rand_list)}')
    answer = prompt.string('Your answer:')
    return is_right(answer, question)
import math
import random

import prompt

from brain_games.engine import MAX_GEN_NUMBER, MIN_GEN_NUMBER, is_right


def get_gcd():
    num_1 = random.randint(MIN_GEN_NUMBER, MAX_GEN_NUMBER)
    num_2 = random.randint(MIN_GEN_NUMBER, MAX_GEN_NUMBER)
    print('Find the greatest common divisor of given numbers.')
    print(f'Question: {num_1} {num_2}')
    answ = prompt.string('Your answer:')
    right_answ = math.gcd(num_1, num_2)
    return is_right(answ, right_answ)
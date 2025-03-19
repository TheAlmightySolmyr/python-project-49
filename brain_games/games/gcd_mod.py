import math
import random

import prompt

from brain_games.cli import is_right


def gcd_game():
    n1 = random.randint(1, 99)
    n2 = random.randint(1, 99)
    print('Find the greatest common divisor of given numbers.')
    print(f'Question: {n1} {n2}')
    answ = prompt.string('Your answer:')
    right_answ = math.gcd(n1, n2)
    return is_right(answ, right_answ)
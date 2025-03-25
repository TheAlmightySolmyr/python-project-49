import math
import random

from brain_games.engine import MAX_GEN_NUMBER, MIN_GEN_NUMBER


def get_gcd():
    num_1 = random.randint(MIN_GEN_NUMBER, MAX_GEN_NUMBER)
    num_2 = random.randint(MIN_GEN_NUMBER, MAX_GEN_NUMBER)
    question = f'{num_1} {num_2}'
    print('Find the greatest common divisor of given numbers.')
    right_answer = math.gcd(num_1, num_2)
    return question, right_answer
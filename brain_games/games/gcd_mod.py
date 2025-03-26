import math
import random

MIN_GEN_NUMBER = 1
MAX_GEN_NUMBER = 99
GCD_RULES = 'Find the greatest common divisor of given numbers.'


def get_gcd():
    num_1 = random.randint(MIN_GEN_NUMBER, MAX_GEN_NUMBER)
    num_2 = random.randint(MIN_GEN_NUMBER, MAX_GEN_NUMBER)
    question = f'{num_1} {num_2}'
    right_answer = math.gcd(num_1, num_2)
    return question, str(right_answer)
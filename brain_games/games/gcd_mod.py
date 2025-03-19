import math
import random

import prompt


def gcd_game():
    n1 = random.randint(1, 99)
    n2 = random.randint(1, 99)
    result = 0
    print('Find the greatest common divisor of given numbers.')
    print(f'Question: {n1} {n2}')
    answ = prompt.string('Your answer:')
    right_answ = math.gcd(n1, n2)
    if int(answ) == right_answ:
        result = 1
    else:
        print(f'{answ} is wrong answer ;(. Correct answer was {right_answ}')
    return result
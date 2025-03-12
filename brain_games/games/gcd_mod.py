import math
import random

import prompt

from brain_games.cli import welcome_user


def gcd_test():
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


def gcd_game():
    name = welcome_user()
    result = 0
    for _ in range(3):
        if gcd_test() == 1:
            print('Correct!')
            result = result + 1
        else:
            print(f'Let\'s try again, {name}!')
            break
    if result == 3:
        print(f'Congratulations, {name}!')
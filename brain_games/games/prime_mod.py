import random

import prompt

from brain_games.engine import MAX_GEN_NUMBER, MIN_GEN_NUMBER, is_right


def is_prime(num):
    result = 0
    for i in range(1, num + 1):
        if num % i == 0:
            result = result + 1
    if result == 2:
        return True
    else:
        return False


def get_prime():
    num = random.randint(MIN_GEN_NUMBER, MAX_GEN_NUMBER)
    print('Answer "yes" if given number is prime. Otherwise answer "no".')
    print(f'Question: {num}')
    answ = prompt.string('Your answer:')
    checked_num = is_prime(num)
    right_answ = 'yes' if checked_num else 'no'
    return is_right(answ, right_answ)
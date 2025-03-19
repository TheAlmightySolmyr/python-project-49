import random

import prompt

from brain_games.cli import is_right


def is_prime(num):
    result = 0
    for i in range(1, num + 1):
        if num % i == 0:
            result = result + 1
    if result == 2:
        return True
    else:
        return False


def prime_game():
    num = random.randint(1, 4000)
    print('Answer "yes" if given number is prime. Otherwise answer "no".')
    print(f'Question: {num}')
    answ = prompt.string('Your answer:')
    checked_num = is_prime(num)
    right_answ = 'yes' if checked_num else 'no'
    return is_right(answ, right_answ)
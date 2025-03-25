import random

from brain_games.engine import MAX_GEN_NUMBER, MIN_GEN_NUMBER


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
    question = random.randint(MIN_GEN_NUMBER, MAX_GEN_NUMBER)
    print('Answer "yes" if given number is prime. Otherwise answer "no".')
    right_answer = 'yes' if is_prime(question) else 'no'
    return question, right_answer
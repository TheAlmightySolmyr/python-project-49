import random

MIN_GEN_NUMBER = 1
MAX_GEN_NUMBER = 99
PRIME_RULES = 'Answer "yes" if given number is prime. Otherwise answer "no".'


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
    right_answer = 'yes' if is_prime(question) else 'no'
    return question, right_answer
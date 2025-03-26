import random

MIN_GEN_NUMBER = 1
MAX_GEN_NUMBER = 99
EVEN_RULES = 'Answer "yes" if the number is even, otherwise answer "no".'


def is_even(num: int):
    return num % 2 == 0


def get_even():
    question = random.randint(MIN_GEN_NUMBER, MAX_GEN_NUMBER)
    right_answer = 'yes' if is_even(question) else 'no'
    return question, right_answer
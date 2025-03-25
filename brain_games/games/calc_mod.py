import random

from brain_games.engine import MAX_GEN_NUMBER, MIN_GEN_NUMBER, OPERATORS


def calculate(num_1, num_2, operator):
    if operator == '+':
        return num_1 + num_2
    if operator == '-':
        return num_1 - num_2
    if operator == '*':
        return num_1 * num_2


def get_calc():
    random_operator = random.choice(OPERATORS)
    num_1 = random.randint(MIN_GEN_NUMBER, MAX_GEN_NUMBER)
    num_2 = random.randint(MIN_GEN_NUMBER, MAX_GEN_NUMBER)
    question = f'{num_1} {random_operator} {num_2}'
    right_answer = calculate(num_1, num_2, random_operator)
    return question, right_answer
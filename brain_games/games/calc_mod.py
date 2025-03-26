import random

MIN_GEN_NUMBER = 1
MAX_GEN_NUMBER = 99
OPERATORS = ('-', '+', '*')
CALC_RULES = 'What is the result of the expression?'


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
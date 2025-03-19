import random

import prompt

from brain_games.cli import is_right

from brain_games.engine import MIN_GEN_NUMBER, MAX_GEN_NUMBER, OPERATORS


def calculate(num_1, num_2, operator):
    match operator:
        case '+':
            return num_1 + num_2
        case '-':
            return num_1 - num_2
        case '*':
            return num_1 * num_2


def get_calc():
    random_operator = random.choice(OPERATORS)
    num_1 = random.randint(MIN_GEN_NUMBER, MAX_GEN_NUMBER)
    num_2 = random.randint(MIN_GEN_NUMBER, MAX_GEN_NUMBER)
    qst = f'{num_1} {random_operator} {num_2}'
    right_answer = calculate(num_1, num_2, random_operator)
    print('What is the result of the expression?')
    print(f'Question: {qst}')
    answer = prompt.string('Your answer:')
    return is_right(answer, right_answer)
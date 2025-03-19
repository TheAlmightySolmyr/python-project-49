import random

import prompt

from brain_games.cli import is_right


def calc_game():
    operators = ['-', '+', '*']
    num_1 = random.randint(1, 99)
    num_2 = random.randint(1, 99)
    qst = (str(num_1) + ' ' + random.choice(operators) + ' ' + str(num_2))
    right_answ = eval(qst)
    print('What is the result of the expression?')
    print(f'Question: {qst}')
    answ = prompt.string('Your answer:')
    return is_right(answ, right_answ)
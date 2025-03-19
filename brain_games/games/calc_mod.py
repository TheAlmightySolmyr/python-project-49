import random

import prompt


def calc_game():
    operators = ['-', '+', '*']
    num_1 = random.randint(1, 99)
    num_2 = random.randint(1, 99)
    qst = (str(num_1) + ' ' + random.choice(operators) + ' ' + str(num_2))
    print('What is the result of the expression?')
    print(f'Question: {qst}')
    answ = prompt.string('Your answer:')
    result = 0
    if int(answ) == eval(qst):
        result = 1
    else:
        print(f'{answ} is wrong answer ;(. Correct answer was {eval(qst)}')
    return result
import random

import prompt

from brain_games.cli import welcome_user


def calc_game_func():
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


def calc_game():
    name = welcome_user()
    result = 0
    for _ in range(3):
        if calc_game_func() == 1:
            print('Correct!')
            result = result + 1
        else:
            print(f'Let\'s try again, {name}!')
            break
    if result == 3:
        print(f'Congratulations, {name}!')
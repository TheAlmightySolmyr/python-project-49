import random

import prompt

from brain_games.cli import name

def calc_game_func():
    operators = ['-','+','*']
    num_1 = random.randint(1,99)
    num_2 = random.randint(1,99)
    question = (str(num_1) + random.choice(operators) + str(num_2))
    print('What is the result of the expression?')
    print(f'Question: {question}')
    answer = prompt.string('Your answer:')
    result = 0
    if int(answer) == eval(question):
        result = 1
    else:
        print(f'{answer} is wrong answer ;(. Correct answer was {eval(question)})')
    return result

def calc_game():
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
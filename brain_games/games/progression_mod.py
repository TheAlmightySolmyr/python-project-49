import random

import prompt

from brain_games.cli import welcome_user


def progression_test():
    start = random.randint(1, 99)
    step = random.randint(1, 99)
    rand_list = [start + i * step for i in range(10)]
    rand_index = random.randint(0, 9)
    question = rand_list[rand_index]
    rand_list[rand_index] = '..'
    print('What number is missing in the progression?')
    str_rand_list = [str(i) for i in rand_list]
    print(f'Question: {' '.join(str_rand_list)}')
    answer = prompt.string('Your answer:')
    result = 0
    if int(answer) == question:
        result = 1
    else:
        print(f'{answer} is wrong answer ;(. Correct answer was {question}')
    return result
    

def progression_game():
    name = welcome_user()
    result = 0
    for _ in range(3):
        if progression_test() == 1:
            print('Correct!')
            result = result + 1
        else:
            print(f'Let\'s try again, {name}!')
            break
    if result == 3:
        print(f'Congratulations, {name}!')
import random

import brain_main
import prompt

from brain_games.cli import name


def is_even(num: int):
    
    if num % 2 == 0:
        return True
    else:
        return False


def even_game():
    print('Answer "yes" if the number is even, otherwise answer "no".')
    question_num = random.randint(1, 99)
    print(f'Question:{question_num}')
    answer = prompt.string('Your answer:')
    result = 0
    if is_even(question_num) == True and answer.lower() == 'yes':
        result = 1
    elif is_even(question_num) == True and answer.lower() == 'no':
        result = 0
    elif is_even(question_num) == False and answer.lower() == 'no':
        result = 1
    elif is_even(question_num) == False and answer.lower() == 'yes':
        result = 0
    return result


def the_game():
    for x in range(3):
        if even_game() == 1:
            print('Correct!')
        else:
            print(f'This is the wrong answer. Try again, {name}!')
            break
    if x == 2:
        print(f'Congratulations, {name}!') 


brain_main.main()
the_game()
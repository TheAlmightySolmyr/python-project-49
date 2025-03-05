import random

import prompt

from brain_games.cli import welcome_user


def is_even(num: int):
    
    if num % 2 == 0:
        return True
    else:
        return False


def even_game():
    print('Answer "yes" if the number is even, otherwise answer "no".')
    question_num = random.randint(1, 99)
    print(f'Question: {question_num}')
    answer = prompt.string('Your answer:')
    result = 0
    if is_even(question_num) is True and answer.lower() == 'yes' or is_even(question_num) is False and answer.lower() == 'no':
        result = 1
    elif is_even(question_num) is True and answer.lower() == 'no' or is_even(question_num) is False and answer.lower() == 'yes':
        result = 0
        if answer.lower() == 'yes':
            print(f"{answer} is wrong answer ;(. Correct answer was 'no'")
        elif answer.lower() == 'no':
            print(f"{answer} is wrong answer ;(. Correct answer was 'yes'")
    return result


def the_game():
    name = welcome_user()
    result = 0
    for _ in range(3):
        if even_game() == 1:
            print('Correct!')
            result = result + 1
        else:
            print(f'Let\'s try again, {name}!')
            break
    if result == 3:
        print(f'Congratulations, {name}!') 
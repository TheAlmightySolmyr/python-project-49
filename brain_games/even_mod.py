import random

import prompt

from brain_games.cli import welcome_user


def is_even(num: int):
    return num % 2 == 0


def even_game():
    print('Answer "yes" if the number is even, otherwise answer "no".')
    question_num = random.randint(1, 99)
    print(f'Question: {question_num}')
    answer = prompt.string('Your answer:')
    correct_answer = 'yes' if is_even(question_num) else 'no'
    result = 0
    if answer == correct_answer:
        result = 1
    else:
        print(f"{answer} is wrong answer ;(. Correct answer was '{correct_answer}'")
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
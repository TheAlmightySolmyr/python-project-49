import random

import prompt

from brain_games.cli import welcome_user


def is_prime(num):
    result = 0
    for i in range(1, num + 1):
        if num % i == 0:
            result = result + 1
    if result == 2:
        return True
    else:
        return False


def prime_test():
    num = random.randint(1, 4000)
    print('Answer "yes" if given number is prime. Otherwise answer "no".')
    print(f'Question: {num}')
    answ = prompt.string('Your answer:')
    checked_num = is_prime(num)
    right_answ = 'yes' if checked_num else 'no'
    result = 0
    if answ == right_answ:
        result = 1
    else:
        print(f"{answ} is wrong answer ;(. Correct answer was '{right_answ}'")
    return result


def prime_game():
    name = welcome_user()
    result = 0
    for _ in range(3):
        if prime_test() == 1:
            print('Correct!')
            result = result + 1
        else:
            print(f'Let\'s try again, {name}!')
            break
    if result == 3:
        print(f'Congratulations, {name}!')
        
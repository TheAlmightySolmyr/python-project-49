from brain_games.cli import name
import math
import random
import prompt

def gcd_test():
    num_1 = random.randint(1,99)
    num_2 = random.randint(1,99)
    result = 0
    print('Find the greatest common divisor of given numbers.')
    print(f'Question: {num_1} and {num_2}')
    answer = prompt.string('Your answer:')
    if int(answer) == math.gcd(num_1, num_2):
        result = 1
    else:
        print(f'{answer} is wrong answer ;(. Correct answer was {math.gcd(num_1, num_2)}')
    return result


def gcd_game():
    result = 0
    for _ in range(3):
        if gcd_test() == 1:
            print('Correct!')
            result = result + 1
        else:
            print(f'Let\'s try again, {name}!')
            break
    if result == 3:
        print(f'Congratulations, {name}!')
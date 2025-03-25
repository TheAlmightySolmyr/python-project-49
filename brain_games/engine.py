import prompt

from brain_games.cli import welcome_user

MIN_GEN_NUMBER = 1
MAX_GEN_NUMBER = 99
OPERATORS = ('-', '+', '*')


def run_three_time(func):
    name = welcome_user()
    print('What is the result of the expression?')
    for _ in range(3):
        qst, right_answ = func()
        print(f'Question: {qst}')
        answ = prompt.string('Your answer:')
        if str(right_answ) == str(answ):
            print('Correct!')
        else:
            print(f'{answ} is wrong answer ;(. Correct answer was {right_answ}')
            print(f'Let\'s try again, {name}!')
            return
            
    print(f'Congratulations, {name}!')
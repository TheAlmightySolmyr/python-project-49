import prompt

from brain_games.cli import welcome_user


def run_game(func, rules):
    name = welcome_user()
    print(rules)
    for _ in range(3):
        qst, right_answ = func()
        print(f'Question: {qst}')
        answ = prompt.string('Your answer:')
        if right_answ == answ.lower():
            print('Correct!')
        else:
            print(f'{answ} is wrong answer ;(. Correct answer was {right_answ}')
            print(f'Let\'s try again, {name}!')
            return
            
    print(f'Congratulations, {name}!')
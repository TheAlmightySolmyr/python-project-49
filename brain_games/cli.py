import prompt


def welcome_user():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    return name


def run_three_time(func):
    name = welcome_user()
    result = 0
    for _ in range(3):
        if func() == 1:
            print('Correct!')
            result = result + 1
        else:
            print(f'Let\'s try again, {name}!')
            break
    if result == 3:
        print(f'Congratulations, {name}!')


def is_right(answer, right_answer):
    fail = f'{answer} is wrong answer ;(. Correct answer was {right_answer}'
    result = 0
    if isinstance(right_answer, str):
        if str(answer) == right_answer:
            result = 1
        else:
            print(fail)
    elif isinstance(right_answer, int):
        if int(answer) == right_answer:
            result = 1
        else:
            print(fail)
    return result
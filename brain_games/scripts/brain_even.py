import random, prompt

def is_even(num:int):
    if num % == 0:
        return True
    else:
        return False

def even_game():
    result = randint(1,99)
    answer = input()
    if is_even(result) == True and answer.lower() == 'yes':
        print(f'Correct!')
    else:
        print(f'''{answer} is wrong answer
        Let's try again!''')

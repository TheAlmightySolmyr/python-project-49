import random, prompt

def is_even(num:int):
    
    if num % 2 == 0:
        return True
    else:
        return False

def even_game():
    print(f'Answer "yes" if the number is even, otherwise answer "no".')
    question = random.randint(1,99)
    print(f'Question:{question}')
    answer = input()
    result = None
    if is_even(question) == True and answer.lower() == 'yes':
        result = True
    elif is_even(question) == True and answer.lower() == 'no':
        result = False
    elif is_even(question) == False and answer.lower() == 'no':
        result = True
    elif is_even(question) == False and answer.lower() == 'yes':
        result = False
    match result:
        case True:
            print('Correct!')
        case False:
            print(f'{answer} is wrong answer. Try again!')

def the_game():
    for _ in range(4):
        result = even_game()
        if result == False:
            break
    return 'Congratulations!'

the_game()
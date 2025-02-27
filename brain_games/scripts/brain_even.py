import random


def is_even(num: int):
    
    if num % 2 == 0:
        return True
    else:
        return False


def even_game():
    print('Answer "yes" if the number is even, otherwise answer "no".')
    question = random.randint(1, 99)
    print(f'Question:{question}')
    answer = input()
    result = True
    if is_even(question) == True and answer.lower() == 'yes':
        result = True
    elif is_even(question) == True and answer.lower() == 'no':
        result = False
    elif is_even(question) == False and answer.lower() == 'no':
        result = True
    elif is_even(question) == False and answer.lower() == 'yes':
        result = False
    return result


def the_game():
    for x in range(3):
        if even_game() == True:
            print('Correct!')
        else:
            print('This is the wrong answer. Try again!')
            break
    if x == 2:
        print('Congratulations!') 


the_game()
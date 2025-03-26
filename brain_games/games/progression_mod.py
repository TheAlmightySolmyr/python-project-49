import random

MIN_GEN_NUMBER = 1
MAX_GEN_NUMBER = 99
PROGRESSION_LEN = 10
PROGRESSION_RULES = 'What number is missing in the progression?'


def get_progression():
    start = random.randint(MIN_GEN_NUMBER, MAX_GEN_NUMBER)
    step = random.randint(MIN_GEN_NUMBER, MAX_GEN_NUMBER)
    rand_list = [start + i * step for i in range(PROGRESSION_LEN)]
    rand_index = random.randint(0, len(rand_list) - 1)
    right_answer = rand_list[rand_index]
    rand_list[rand_index] = '..'
    str_rand_list = [str(i) for i in rand_list]
    question = ' '.join(str_rand_list)
    return question, str(right_answer)
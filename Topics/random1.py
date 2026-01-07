import random

def get_answer(answer_number):
    if answer_number == 1:
        return "you got chocolate"
    elif answer_number == 2:
        return "you got pen"
    elif answer_number == 3:
        return "you got eraser"
    elif answer_number == 4:
        return "you got cycle"
    elif answer_number == 5:
        return "you got ball"
    elif answer_number == 6:
        return "you got book"
    elif answer_number == 7:
        return "you got money"
    elif answer_number == 8:
        return "you got game"
    
print(get_answer(random.randint(1,8)))
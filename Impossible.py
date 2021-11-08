import random
import time
game = True
from end_message import end
print("Welcome to Impossible mode!")
while game:
    print('You have 1 guess...')
    time.sleep(2)
    print('Good Luck')
    number = random.randint(0,100)
    print('Please wait...')
    time.sleep(3)
    print('...Im thinking of a number between 0 and 100... ')
    time.sleep(3)
    guess = True
    while guess:
        user_number = int(input('What is my number?: '))
        if user_number != number:
            if user_number in range(number - 10, number + 10):
                message1 = f'Soooooo close!! You nearly defeated the game!\nMy Number was {number} !\nWould you like to play again?: '
                guess = end(message1)
            else:
                message1 = f'Unlucky. You were nowhere near.\nMy Number was {number} !\nWould you like to play again?: '
                guess = end(message1)
        if number == user_number:
            message1 = '''ARE YOU HUMAN!!!!????
yOU HavE bROkEN The GAme!
Well done for completing Jamie's Guess the Number
You shall go down in the hall of fame!
Would you like to play again?'''
            guess = end(message1)
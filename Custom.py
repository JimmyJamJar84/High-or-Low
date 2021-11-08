import random
import time
game = True
def guesses(message):
    error = False
    while error == False:
        try:
            num_guesses = int(input(message))
            return num_guesses
            break

        except ValueError:
            print('Enter a number only')
            error = False
def end(message1):
    play = input(message1)
    if play == 'no':
        diff_mode = input('Would you like to pick a different mode?: ')
        if diff_mode == 'yes':
            import Home
        if diff_mode == 'no':
            quit()
    if play == 'yes':
        return False
print("Welcome to Jamie's Guess The Number!")
while game:
    message = 'How many guesses would you like?: '
    num_guesses = guesses(message)
    number = random.randint(0,100)
    print('Please wait...')
    time.sleep(3)
    print('...Im thinking of a number between 0 and 100... ')
    time.sleep(3)
    guess = True
    while guess:
        user_number = int(input('...What is my number?: '))
        if user_number < number:
            print('Too low')
        if user_number > number:
            print('Too high')
        if number != user_number:
            num_guesses = num_guesses-1
            print(f'UnLuCkY! You have {num_guesses} guesses left!')
        if num_guesses == 0:
            message1 = 'You have used up all of your lives! Too bad! Would you like to play again?: '
            guess = end(message1)
        if number == user_number:
            message1 = 'Well Done, you guessed correctly! Would you like to play again?: '
            guess = end(message1)
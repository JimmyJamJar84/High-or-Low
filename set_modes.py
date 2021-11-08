def game(mode_name,num_guesses):
    import random
    import time
    game = True
    from end_message import end
    print(f"Welcome to {mode_name} mode!")
    while game:
        print(f'You have {num_guesses} guesses...')
        number = random.randint(0,100)
        print('Please wait...')
        time.sleep(2)
        print('...Im thinking of a number between 0 and 100... ')
        time.sleep(2)
        guess = True
        while guess:
            user_number = int(input('What is my number?: '))
            if user_number < number:
                print('Too low!')
            if user_number > number:
                print('Too high!')
            if number != user_number:
                num_guesses -= 1
                print(f'UnLuCkY! You have {num_guesses} guesses left!')
            if num_guesses == 0:
                message1 = f'You have used up all of your lives!\nMy number was {number}\nWould you like to play again?: '
                guess = end(message1)
            if number == user_number:
                message1 = 'WeLl DoNe, you guessed correctly! Would you like to play again?: '
                guess = end(message1)
def end(message1):
    play = input(message1)
    if play == 'no':
        diff_mode = input('Would you like to pick a different mode?: ')
        if diff_mode == 'yes':
            import Home
        if diff_mode == 'no':
            quit()
    elif play == 'yes':
        return False
    else:
        print('error')
        quit()
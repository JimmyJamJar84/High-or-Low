import time
from playsound import playsound
p = playsound
from set_modes import game
def modes():
    mode = int(input('''What mode would you like to play?:
1) Super easy
2) Easy
3) Normal
4) Hard
5) Super Hard
6) Impossible
7) Custom
'''))
    from set_modes import game
    if mode == 1:
        game('Super Easy', 30)
    elif mode == 2:
        game('Easy', 17)
    elif mode == 3:
        game('Normal', 10)
    elif mode == 4:
        game('Hard', 5)
    elif mode == 5:
        game('Super Hard', 2)
    elif mode == 6:
        import Impossible
    elif mode == 7:
        import Custom
print('A JimmyJamJar creation...')
p("Xbox achievement.mp3", False)
time.sleep(1)
print("Welcome to Jamie's Guess The Number!")
time.sleep(1)
menu= int(input('''Main Menu:
1) Quick play
2) Game modes
'''))
if menu == 1:
    game('Normal', 10)
if menu == 2:
    modes()







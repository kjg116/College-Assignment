import random

def game():
    throw = int(input('Choose a throw to play: '))

    x = random.randint(1,3)

    if x == 1 and throw == 1:
        print("Computer played rock.")
        print("Tie.")
    elif x == 2 and throw == 2:
        print('Computer played paper.')
        print('Tie.')
    elif x == 3 and throw == 3:
        print('Computer played scissors.')
        print('Tie.')
    elif x == 1 and throw == 2:
        print('Computer played rock.')
        print('You Win!')
    elif x == 1 and throw == 3:
        print('Computer played rock.')
        print('You lose.')
    elif x == 2 and throw == 1:
        print('Computer played paper.')
        print('You lose.')
    elif x == 2 and throw == 3:
        print('Computer played paper.')
        print('You win!')
    elif x == 3 and throw == 2:
        print('Computer played scissors.')
        print('You lose.')
    elif x == 3 and throw == 1:
        print('Computer played scissors.')
        print('You win!')

def main():
    keep_playing = 'y'

    while keep_playing == "y":
        print('Welcome to rock-paper-scissors!')
        print('You can play one of the following throws:')
        print('1. Rock')
        print('2. Paper')
        print('3. Scissors')

        game()

        print('')

        keep_playing = input("Play again? (enter 'y'): ")

        print("")

main()
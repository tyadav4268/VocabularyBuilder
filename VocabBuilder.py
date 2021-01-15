import game
from gameResources import get_random_word_meaning

name = input("What is your name? ")
print(f"Hello {name}! Welcome to The Vocab_Builder")
print(f"Word of the Day: {get_random_word_meaning()}")
print()

while True:
    play_choice = input("Shall we enter the Arena? Y/N: ")
    if play_choice == 'y' or play_choice == 'Y':
        print("Now let's start the Game")
        game.play_game()
        print("Thank You ! Have a nice day!")
        break
    elif play_choice == 'N' or play_choice == 'n':
        print("Thank You ! Have a nice day!")
        break
    else:
        print("Invalid Input!")
        continue

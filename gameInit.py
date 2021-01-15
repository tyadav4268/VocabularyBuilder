def get_num_attempts():
    '''Get user-inputted number of incorrect attempts for the game'''
    while True:
        user_input = input("How many incorrect attempts should be allowed? [1-24]: ")
        try:
            num_attempts = int(user_input)
            if 1 <= num_attempts <= 24:
                return num_attempts
            else:
                print("Min attempt is 1 and Max is 24. Please enter a value between 1-24.")
        except ValueError:
            print("Invalid input! Please enter an integer.")

def play_again():
    while True:
        user_choice = input("Want to play again? y/n: ")
        if user_choice == 'y' or user_choice =='Y':
            return 1
        elif user_choice == 'n' or user_choice == 'N':
            return 0
        else:
            print("Invalid input! Please enter y/n")

# print(get_num_attempts())
# print(play_again())

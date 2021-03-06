from gameInit import get_num_attempts, play_again
from gameResources import get_random_word_meaning, match_words

def play_game():
    while True:
        num_attempts = get_num_attempts()
        guess_word, meaning = get_random_word_meaning()
        print("The meaning of word is: ",meaning)
        print("Guess the word")
        while num_attempts > 0:
            user_word = input("Enter your guess: ").lower()
            result = match_words(user_word, guess_word)
            if result == 1:
                print("Congratulations! Your guess is correct!!")
                break
            else:
                print("Computer says: ",result)
                num_attempts -= 1
                print("Remaining attempts: ", num_attempts)
                continue
        if num_attempts == 0:
            print(f"You couldn't guess it right!\nThe word is {guess_word}")
        choice = play_again()
        if choice == 1:
            continue
        else:
            break

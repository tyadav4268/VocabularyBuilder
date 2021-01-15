import random

fileName = "dict.txt"

def getRandomWordMeaning():
    '''returns a tuple of a random word and its meaning'''
    totalWords = 0
    currentData = None
    with open(fileName, "r") as f:
        for line in f:
            totalWords += 1
            if random.randint(1, totalWords) == 1:
                currentData = line.strip().lower()
    wordMeaning = currentData.split(',')
    word = wordMeaning[0]
    meaning = wordMeaning[1]
    return word, meaning
# print(getRandomWordMeaning())

def game_hint(guess_word):
    return f"Hint: Length of the word is {len(guess_word)} "

# print(game_hint("guess"))

def match_words(user_word, guess_word):
    if user_word.lower() == guess_word.lower():
        return 1
    elif len(user_word) <= len(guess_word):
        word = ''
        for i in range(len(guess_word)):
            try:
                if guess_word[i] == user_word[i]:
                    word += guess_word[i]
                else:
                    word += '*'
            except IndexError:
                word += '*'
        return word
    else:
        print(game_hint(guess_word))
        return "Length of your guess word is greater than original word! "


# print(match_words("fanmilyofsnakes", "fanmily"))

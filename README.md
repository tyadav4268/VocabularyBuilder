# VocabularyBuilder

## Vocabulary Builder is a project written in python.
## The Vocabulary Builder provides a word of the day and a game where the user has to guess the word from the given meaning of a word and other hints.
---
## File Layout:
- **VocabBuilder.py** : 
    - It uses **get_random_word_meaning()** function from the file **gameResources.py** to display a random new word each time it is run. 
    - This is the main file which calls the **play_game()** function from the file **game.py**. 
    
- **game.py**: 
  - This is the file containing **play_game()** function.
  - Uses **get_num_attempts()** and **play_again()** function from the file **gameInit.py** 
  - Uses **get_random_word_meaning()** and **match_words()** function from the file **gameResources.py**.
    
- **gameInit.py**:
  - This file contains the definition of the two functions **get_num_attempts()** and **play_again()**. 
    
- **gameResources.py**: 
  - This file contains the definition of the two functions **get_random_word_meaning()** and **match_words()**, it also contains a function **game_hint()** which is used by the function **match_words()**.
    
- **dict.txt**: 
  - This is a text file which contains a word and its meaning separated by a **comma(',')** in each line.
---

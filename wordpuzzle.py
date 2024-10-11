# Victoria Lutz
# My creativity is making it dictionary with lists and different words so it's not always just one word

import random

print('Welcome to the guess my word game')
# dictionary to randomize word
game_dict = {'scriptures': ['nephi', 'lehi', 'mosiah', 'alma'],
             'sports': ['basketball', 'football', 'soccer', 'mma',],
             'colors': ['red', 'blue', 'green', 'purple',], }
# randomize the category
game_category = []
for key in game_dict:
    game_category.append(key)


my_category = random.choice(game_category)
game_word = random.choice(game_dict[my_category])


print(
    f'Guess a {len(game_word)} number word from the following category: {my_category}')
# this is to create the dashes

blank_word = []
for i in range(len(game_word)):
    blank_word.append('-')

print("".join(blank_word))

guess = ''
guess_count = 0

for attempt in range(1, 7):
    guess = input().lower()

    guess_count += 1
    if guess == game_word:
      print(f"Correct, the game word was {game_word}. You guessed it in {guess_count} tries!")
      quit()
    elif len(guess) != len(game_word):
      print(f"You've entered the wrong length of word. Please enter a {len(game_word)} letter word: ")
    elif guess_count > 6:
      print(f"You ran out of tries! Sorry, your word was {game_word}")
      quit()
    else:
        for i in range(len(guess)):
            if guess[i] == game_word[i]:
            
                print(guess[i].upper(), end=' ')
            elif guess[i] in game_word:
             print(guess[i], end=' ')  
            else:
             print(end=' ')


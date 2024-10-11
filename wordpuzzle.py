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

# TODO from dad. This can just be a string. You can use + to join strings it
# is called concatenation. So this could be:
# blank_word = ""
# for i in range(len(game_word)):
#   blank_word += "_ " # this is the shorthand, could also be `blank_word = blank_word + "_ "`
# print(blank_word)
blank_word = []
for i in range(len(game_word)):
    blank_word.append('-')

print("".join(blank_word))

guess = ''
# TODO from dad. You weren't incrementing guess_count, but were attempt. Attempt is set as part of the
# for loop, so I've commented it out up here, and change the code below to increment guess_count, now
# it should display correctly at the end of the game.
guess_count = 0
# attempt = 0

# TODO from dad. You could use a while loop here. You would just set a variable to True, and when the game ends
# change the variable to False. This could result in unlimited tries, so you might not want that.
# That would look something like:
# keep_looping = True
# while keep_looping:
#   guess = input().lower()
for attempt in range(1, 7):
    guess = input().lower()

    # TODO from dad. You should reorder your code. Check for all the things that end the game
    # first, then your individual letter inputs. This won't make a big difference here, but in
    # a bigger program will save a lot of computing time. Add one to guess_count at the very first, then you
    # don't have to include it in every check. Then I would  check if they guessed correctly first,
    # then you just have to notify them that they won. Then I would compare len(guess) == len(game_word)
    # and if they are different request a new input. You can still count this as an
    # attempt but will fix some problems with what to do with extra letters.
    # Something like:

    guess_count += 1
    # if guess == game_word:
    #   print(f"Correct, the game word was {game_word}. You guessed it in {guess_count} tries!")
    # elif len(guess) != len(game_word):
    #   print(f"You've entered the wrong length of word. Please enter a {len(game_word)} letter word: ")
    # elif guess_count > 6:
    #   print(f"You ran out of tries! Sorry, your word was {game_word}")
    # else:
    # TODO from dad. If you check if the two words are the same length you can just use a `for i in range(len(game_word)):`
    for i in range(min(len(guess), 12)):
        if guess[i] == game_word[i]:
            # TODO from dad. I don't think you need the end= here. `print(guess[i].upper(), " ")` should work fine.
            print(guess[i].upper(), end=' ')
        elif guess[i] in game_word:
            print(guess[i], end=' ')  # TODO from dad. Don't need the end= here
        else:
            print(end=' ')  # TODO from dad. Don't need the end= here

# TODO from dad. In my example above this is already taken care of and can be deleted. These need to be checked inside
# the loop, or it will go through 7 times, then hit this check after. If they guess correctly at first it will
# never hit until they've guessed all 7 times.
if guess == game_word:
    print(
        f'Correct the game word was {game_word} you guessed it in {guess_count} tries! ')
elif attempt == 6:
    print(f'You ran out of tries! Sorry your word was {game_word}')

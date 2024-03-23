#Step 2

import random

word_list = ["aardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)

display = []
word_lenth = len(chosen_word)
for _ in range(word_lenth):
    display += "_"
print(display)
#Testing code
print(f'Pssst, the solution is {chosen_word}.')

#TODO-1: - Create an empty List called display.
#For each letter in the chosen_word, add a "_" to 'display'.
#So if the chosen_word was "apple", display should be ["_", "_", "_", "_", "_"] with 5 "_" representing each letter to guess.

end_of_game = False
while not end_of_game:
    guess = input("Guess a letter: ").lower()
    #TODO-2: - Loop through each position in the chosen_word;
    #If the letter at that position matches 'guess' then reveal that letter in the display at that position.
    #e.g. If the user guessed "p" and the chosen word was "apple", then display should be ["_", "p", "p", "_", "_"].
    for position in range(word_lenth):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter
    print(display)
    if "_" not in display:
        end_of_game = True
        print("you win")
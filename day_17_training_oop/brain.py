from words_list import word_list
from art import stages
import random

class Hangman:
    def __init__(self):
        self.chosen_word = ""
        self.display = []
        self.word_length = 0
        self.lives = 6
        self.end_of_game = False
        self.create_the_word()

    def create_the_word(self):
        self.chosen_word = random.choice(word_list)
        self.word_length = len(self.chosen_word)
        self.display = ["_"] * self.word_length

    def guess(self, user_guess):
        if user_guess in self.display:
            print(f"The letter you enter {user_guess} is already in")
        for position in range(self.word_length):
            letter = self.chosen_word[position]
            if letter == user_guess:
                self.display[position] = letter         
        if user_guess not in self.chosen_word:
            print(f"{user_guess} is wrong, you lose one life")
            self.lives -= 1
            if self.lives == 0:
                self.end_of_game = True
                print("You lose.")
        print(f"{' '.join(self.display)}")
        if "_" not in self.display:
            self.end_of_game = True
            print("You win.")
        print(stages[self.lives])

    def is_game_over(self):
        return self.end_of_game
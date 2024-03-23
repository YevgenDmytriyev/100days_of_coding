from art import logo
from brain import Hangman

print(logo)
hangman = Hangman()

while not hangman.is_game_over():
    user_guess = input("Guess a letter: ").lower()
    hangman.guess(user_guess)
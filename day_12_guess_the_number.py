#from art import logo
import random

#print(logo)
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100")

def guess(num_guess):
  guess = int(input("Make a guess:\n"))
  number = int(random.choice(range(1,101)))
  while num_guess > 1:
    if guess != number:
      if number > guess:
        num_guess -= 1
        print("You are too low")
        print(f"You have {num_guess} attempts remaining to guess the number")
      elif number < guess:
        num_guess -= 1
        print("You are too high")
        print(f"You have {num_guess} attempts remaining to guess the number")
      else:
        guess == number
        print(f"You got it! The answer was {number}")
        return
    else:
      guess == number
      print(f"You got it! The answer was {number}")
      return
    guess = int(input("Make a guess:\n"))
  print("You have no more attempts remained")
  print("You lose!")
  return

def start_game():
  choice = input("Choose a difficulty. Type 'e' for easy, 'a' for average, 'h' for hard: ").lower()
  if choice == 'e':
    guess(num_guess = 10)
  elif choice == 'a':
    guess(num_guess = 7)
  elif choice == 'h':
    guess(num_guess = 5)

game_on = False
while not game_on:
  start_game()
  choice = input("Please make your next move: 'y' to play more or 'n' to quit: \n").lower()
  print(logo)
  if choice == 'n':
    break
#from art import logo,vs
import random
#from game_data import data
#from replit import clear

follower_a = 0
follower_b = 0

def choiceA():
  global follower_a
  dict_a = random.choice(data)
  name_a = dict_a['name']
  follower_a = dict_a['follower_count']
  description_a = dict_a['description']
  country_a = dict_a['country']
  return f"Compare A: {name_a}, a {description_a}, from {country_a}"

def choiceB():
  global follower_b, name_b, description_b, country_b
  dict_b = random.choice(data)
  name_b = dict_b['name']
  follower_b = dict_b['follower_count']
  description_b = dict_b['description']
  country_b = dict_b['country']
  return f"Compare B: {name_b}, a {description_b}, from {country_b}"

def game():
  global follower_a, follower_b, name_b, description_b, country_b
  #print(logo)
    # If this isn't the first round, make choiceB of the last round the new choiceA
  if follower_b != 0:
    follower_a = follower_b
    print(f"Compare A: {name_b}, a {description_b}, from {country_b}")
  else:
    print(choiceA())
  #print(vs)
  # Generate choiceB and ensure it's different from choiceA
  while True:
    move_b_text = choiceB()
    if follower_a != follower_b:
        break
  print(move_b_text)

score = 0 
game_on = True  
while game_on:
    #game()
    choice = input("Who have more followers? Type A or B: ").upper()
    if (choice == 'A' and follower_a > follower_b) or (choice == 'B' and follower_b > follower_a):
        score += 1
        #clear()
        print(f"You are right! Current score: {score}")
    else:
        #clear()
        #print(logo)
        print(f"Sorry that's wrong. Final score: {score}")
        game_on = False  
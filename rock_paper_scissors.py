import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
choice = input("Pleae make your chois as 1 for Rock, 2 for Paper and 3 for Scissors :\n")
map = ['rock','paper','scissors']
map[0] = rock
map[1] = paper
map[2] = scissors
pl = (int(choice))-1
co = random.randint(0,2)
comp = map[co]
player = map[pl]
if (choice == "1" and comp == rock) or (choice == "2" and comp == paper) or (choice == "3" and comp == scissors):
  print(f"You choice:\n {player}\n Computer choice:\n {comp}\nYou had a draw!")
elif (choice == "1" and comp == scissors) or (choice == "2" and comp == rock) or (choice == "3" and comp == paper):
  print(f"You choice:\n {player}\n Computer choice:\n{comp}\nYou win!")
else:
  print(f"You choice:\n {player}\n Computer choice:\n{comp}\nYou lose!")

# nested if statement

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print("Leap year.")
        else:
            print("Not leap year.")
    else:
        print("Leap year.")
else:
    print("Not leap year.")
 

# how to make nested if statement with choises
   
choise = input("\nYou have to make your choise, which direction to go: right or left\n").lower()
if choise == "left":
  print("Good choise, now you have to make your other choises")
  choise = input("\nYou have to make your next choise, but this time is not about to go but: swim or wait\n").lower()
  if choise == "wait":
      print("Good choise, now you have to make your other choises")
      choise = input("\nYou have to make your next choise, but this time is not about to Swim\n or wait but about colors: red or blue or yellow\n").lower()
      if choise == "yellow":
        print("Congratulations You Win!!!")
      elif choise == "red":
        print("Burned by fire. Game Over.")
      elif choise == "blue":
        print("Eaten by beasts. Game Over.")
      else:
        print("Game over")
  else:
      print("Attacked by trout. Game Over.")
else:
  print("Fall into a hole.Game Over.")
  
  
# random choices
import random

random_integer = random.randint(1 , 10)
print(random_integer)

random_float = random.random()
print(random_float)


# for statemant
# total count
total = 0    
for number in range(1,101):
    total += number
print(total)

# total count but with step start from 2 up to 100 and with step 2
total = 0
for i in range(2,101,2):
    total += i
print(total)

# total count but only with the numbers which is devided by 2 without residue
total2 = 0
for number in range(1, 101):
    if number % 2 == 0:
        total2 += number
print(total2)
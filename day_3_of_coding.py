# 🚨 Don't change the code below 👇
number = int(input("Which number do you want to check? "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
if number % 2 == 0:
    print("This is an even number.")
else:
    print("This is an odd number.")
    
print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
if height >= 120:
  print("Go ahead body!")
else:
  print("See you soon body!")
  
# 🚨 Don't change the code below 👇
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
BMI = round(weight / height**2)

if BMI <= 18.5:
    print(f"Your BMI is {BMI}, you are underweight.")
elif BMI <= 25:
    print(f"Your BMI is {BMI}, you have a normal weight.")
elif BMI <= 30:
    print(f"Your BMI is {BMI}, you are slightly overweight.")
elif BMI <= 35:
    print(f"Your BMI is {BMI}, you are obese.")
elif BMI > 35:
    print(f"Your BMI is {BMI}, you are obese.")   
else:
    print("Who are you baby")
    
# 🚨 Don't change the code below 👇
year = int(input("Which year do you want to check? "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
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
 

# 🚨 Don't change the code below 👇
print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
total = 0
if size == "S":
    total += 15
    if add_pepperoni == "Y":
        total += 2
    if extra_cheese == "Y":
        total += 1 
elif size == "M":
    total += 20
    if add_pepperoni == "Y":
        total += 3
    if extra_cheese == "Y":
        total += 1  
elif size == "L":
    total += 25
    if add_pepperoni == "Y":
        total += 3
    if extra_cheese == "Y":
        total += 1
else:
    ("See you next time!")
print(f"Your final bill is: ${total}") 

# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
total = 0
l_case_name1 = name1.lower()
l_case_name2 = name2.lower()
names_s = l_case_name1 + l_case_name2
true_count = names_s.count('t') + names_s.count('r') + names_s.count('u') + names_s.count('e')
love_count = names_s.count('l') + names_s.count('o') + names_s.count('v') + names_s.count('e')
score = true_count*10 + love_count
if score < 10 or score > 90:
    print(f"Your score is {score}, you go together like coke and mentos.")
elif score >=40 and score <= 50:
    print(f"Your score is {score}, you are alright together.")
else:
    print(f"Your score is {score}.")

import random

random_integer = random.randint(1 , 10)
print(random_integer)

random_float = random.random()
print(random_float)

new = random_float * 5
print(new)

#Remember to use the random module
#Hint: Remember to import the random module here at the top of the file. 🎲
	 
#Write the rest of your code below this line 👇
random_integer = random.randint(1 , 2)
ran = random_integer
if ran == 1:
    print("Heads")
else:
    print("Tails")
    
# Import the random module here

# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆
# Angela, Ben, Jenny, Michael, Chloe
#Write your code below this line 👇
n = random.randint(0, (len(names))-1)
name = names[n]
print(f"{name} is going to buy the meal today!")

# 🚨 Don't change the code below 👇
row1 = ["⬜️","️⬜️","️⬜️"]
row2 = ["⬜️","⬜️","️⬜️"]
row3 = ["⬜️️","⬜️️","⬜️️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ")
# 🚨 Don't change the code above 👆

#Write your code below this row 👇
move = list(str(position))
row = int(move[1])
col = int(move[0])
map[row -1][col -1] = 'X'
#Write your code above this row 👆

# 🚨 Don't change the code below 👇
print(f"{row1}\n{row2}\n{row3}")
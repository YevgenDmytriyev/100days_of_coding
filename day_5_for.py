#for number in range(1,1,3):
#    print(number)

total = 0    
for number in range(1,101):
    total += number
print(total)
    
#Write your code below this row 👇
total = 0
for i in range(2,101,2):
    total += i
print(total)

total2 = 0
for number in range(1, 101):
    if number % 2 == 0:
        total2 += number
print(total2)

#Write your code below this row 👇
for number in range(1, 101):
    if number % 3 == 0 and number % 5 == 0:
        print("FizzBuzz")
    if number % 3 == 0:
        print("Fizz")
    elif number % 5 == 0:
        print("Buzz")
    else:
        print(number)

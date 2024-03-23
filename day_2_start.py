#Data Types
# 🚨 Don't change the code below 👇
two_digit_number = input("Type a two digit number: ")
# 🚨 Don't change the code above 👆

####################################
#Write your code below this line 👇
num1 = int(two_digit_number[0])
num2 = int(two_digit_number[1])
num = num1 + num2
print(num)

print(3 * (3 +3) / 3 - 3)

# 🚨 Don't change the code below 👇
height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
BMI = int(weight)/ float(height)**2
print(int(BMI))

# 🚨 Don't change the code below 👇
age = input("What is your current age? ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
days = (90 * 365) - (int(age) * 365)
d = days
weeks = (90 * 52) - (int(age) * 52)
w = weeks
month = (90 * 12) - (int(age) * 12) 
m = month
print(f"You have {d} days, {w} weeks, and {m} months left.") 

print("welcome to calculator")
total_bill = input("Please enter the sum of the bill(exp: 214.56): \n")
t = float(total_bill)
percentage_decided = int(input("Please enter the percentage you want to pay(exp: 22): \n"))
per = percentage_decided
percentage = (t/100) * per
p = percentage
total_including_tips = t + p
i = total_including_tips
amount_of_people_to_share = int(input("Please enter amount of people to split the bill(exp:5): \n"))
a = amount_of_people_to_share
amount_to_pay = i / a
atp = amount_to_pay
print(f"Each person needs to pay:{round(atp,2)}")


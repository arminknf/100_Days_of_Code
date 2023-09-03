# 🚨 Don't change the code below 👇
age = input("What is your current age? ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
#print("assuming the age of 90 years")
year_remind = 90 - int(age)
days_remind = year_remind * 365
weeks_remind = year_remind * 52 
months_remind = year_remind * 12

print(f"You have {days_remind} days, {weeks_remind} weeks, and {months_remind} months left.")





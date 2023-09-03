# Import the random module here
import random
# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
#print(len(names))
len_people = len(names)
random_choose = random.randint(0, (len_people - 1))
#print(random_choose)
lucky_name = names[random_choose]
print(f"{lucky_name} is going to buy the meal today!")
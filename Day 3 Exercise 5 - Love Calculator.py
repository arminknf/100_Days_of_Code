# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
name1_low = name1.lower()
name2_low = name2.lower()
t_count1 = name1_low.count('t')
r_count1 = name1_low.count('r')
u_count1 = name1_low.count('u')
e_count1 = name1_low.count('e')

t_count2 = name2_low.count('t')
r_count2 = name2_low.count('r')
u_count2 = name2_low.count('u')
e_count2 = name2_low.count('e')
True_count = t_count1 + r_count1 + u_count1 + e_count1 + t_count2 + r_count2 + u_count2 + e_count2
#print(True_count)

l_count1 = name1_low.count('l')
o_count1 = name1_low.count('o')
v_count1 = name1_low.count('v')
e_count1 = name1_low.count('e')

l_count2 = name2_low.count('l')
o_count2 = name2_low.count('o')
v_count2 = name2_low.count('v')
e_count2 = name2_low.count('e')
Love_count = l_count1 + o_count1 + v_count1 + e_count1 + l_count2 + o_count2 + v_count2 + e_count2
#print(Love_count)

love_scores = int(str(True_count) + str(Love_count))
#print(love_scores)

if love_scores <= 10 or love_scores >= 90:
    print(f"Your score is {love_scores}, you go together like coke and mentos.")
elif love_scores >= 40 and love_scores <= 50:
        print(f"Your score is {love_scores}, you are alright together.")
else:
    print(f"Your score is {love_scores}.")

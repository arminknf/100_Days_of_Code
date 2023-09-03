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
import random
print("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n")

your_choose = int(input("Your choose: "))

pc_choose = random.randint(0,2)

'''if(your_choose == 0):
  print(f"Your chose: {rock}")
elif(your_choose == 1):
  print(f"Your chose: {paper}")
elif(your_choose == 2):
  print(f"Your chose: {scissors}")'''


'''if(pc_choose == 0):
  print(f"PC chose: {rock}")
elif(pc_choose == 1):
  print(f"PC chose: {paper}")
elif(pc_choose == 2):
  print(f"PC chose: {scissors}")
'''
game_images = [rock, paper, scissors]
if(your_choose >= 3 or your_choose < 0):
  print("You type an invalid number, you lose!")
else:
  print(game_images[your_choose])
  print(game_images[pc_choose])

if (your_choose == pc_choose):
  print("It's a draw")
elif(your_choose == 0 and pc_choose == 1):
  print("You lose")
elif(your_choose == 0 and pc_choose == 2):
  print("You win!")
elif(your_choose == 1 and pc_choose == 0):
  print("You win!")
elif(your_choose == 1 and pc_choose == 2):
  print("You lose")
elif(your_choose == 2 and pc_choose == 0):
  print("You lose")
elif(your_choose == 2 and pc_choose == 1):
  print("You win!")






#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91
'''
len_letters = len(letters)
len_symbols = len(symbols)
len_numbers = len(numbers)
password = []

for _ in range(nr_letters):
  cnt_letters = random.randint(0, len_letters - 1)
  selected_letter = letters[cnt_letters]
#  print("Selected letter:", selected_letter)
  password.append(selected_letter)

for _ in range(nr_symbols):
  cnt_symbols = random.randint(0, len_symbols - 1)
  selected_symbols = symbols[cnt_symbols]
#  print("Selected symbols:", selected_symbols)
  password.append(selected_symbols)

for _ in range(nr_numbers):
  cnt_numbers = random.randint(0, len_numbers - 1)
  selected_numbers = numbers[cnt_numbers]
#  print("Selected numbers:", selected_numbers)
  password.append(selected_numbers)

final_password = ''.join(password)
print("Generated password:", final_password)
'''
#Hard Level - Order of characters randomised:

len_letters = len(letters)
len_symbols = len(symbols)
len_numbers = len(numbers)
password = []

for _ in range(nr_letters):
  cnt_letters = random.randint(0, len_letters - 1)
  selected_letter = letters[cnt_letters]
#  print("Selected letter:", selected_letter)
  password.append(selected_letter)

for _ in range(nr_symbols):
  cnt_symbols = random.randint(0, len_symbols - 1)
  selected_symbols = symbols[cnt_symbols]
#  print("Selected symbols:", selected_symbols)
  password.append(selected_symbols)

for _ in range(nr_numbers):
  cnt_numbers = random.randint(0, len_numbers - 1)
  selected_numbers = numbers[cnt_numbers]
#  print("Selected numbers:", selected_numbers)
  password.append(selected_numbers)

random.shuffle(password)
final_password = ''.join(password)
print("Your password is:", final_password)
  
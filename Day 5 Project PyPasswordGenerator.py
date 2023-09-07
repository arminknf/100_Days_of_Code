#password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 
           'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 
           'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 
           'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Easy Level

len_letters = int(len(letters))
len_symbols = int(len(symbols))
len_numbers = int(len(numbers))

storage_password = [] 
hard_password = []
for _ in range(0, nr_letters):
  random_num_list = random.randint(0 ,len_letters-1)
  password_letter = storage_password.append(letters[random_num_list])

for _ in range(0, nr_symbols):
  random_num_list = random.randint(0 ,len_symbols-1)
  password_letter = storage_password.append(symbols[random_num_list])

for _ in range(0, nr_numbers):
  random_num_list = random.randint(0 ,len_numbers-1)
  password_letter = storage_password.append(numbers[random_num_list])

print(f"Easy Password: {''.join(storage_password)}")
random.shuffle(storage_password)
#Hard Level
hard_password = ''.join(storage_password)
print(f"Hard Password: {hard_password}")




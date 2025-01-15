import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&','*', '+']

print("Welcome to the PyPassword Generator!")
user_letters = int(input("How many letters would you like in your password?\n"))
user_symbols = int(input(f"How many symbols would you like?\n"))
user_numbers = int(input(f"How many numbers would you like?\n"))

temp_list=[]
for _ in range(0,user_letters):
    random_character=random.choice(letters)
    temp_list.append(random_character)
for _ in range(0,user_symbols):
    random_symbol=random.choice(symbols)
    temp_list.append(random_symbol)
for _ in range(0,user_numbers):
    random_number=random.choice(numbers)
    temp_list.append(random_number)
random.shuffle(temp_list)
print("".join(temp_list))






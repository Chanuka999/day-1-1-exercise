import random

letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u',
           'v','w','x','y','z']

numbers = ['0','1','2','3','4','5','6','7','8','9']

symbols = ['!','#','$','%','&','(',')','*','+']

print("Welcome to the pyPassword Generator!")
r_letters = int(input("How many letters would you like in your password?\n"))

r_symbols = int(input("How many symbols would you like\n"))

r_numbers= int(input("how many numers would you like?\n"))

password = []

for char in range(1, r_letters + 1):
    password += random.choice(letters)
   
for char in range(1, r_symbols + 1):
    password += random.choice(symbols)

for char in range(1, r_numbers + 1):
    password += random.choice(numbers)

#print(password)
random.shuffle(password)
#print(password)

new_password = ""
for char in password:
    new_password +=char
    
print(f"Your password is : {new_password}")
   

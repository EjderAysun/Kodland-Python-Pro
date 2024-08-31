# A technical exercise!
print()
#----------
# Create a variable containing all the characters that the user's password can contain
characters = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
# Create a variable and ask the user to enter the length of the password
password_len = int(input("Please enter the length of the password: "))
# Create a variable where the program will store the generated password
password = ""
# Use a loop and the 'random' library to select a random character from the 'characters' variable and add it to the variable with the generated password
import random
for i in range(password_len):
    password += random.choice(characters)
# Print the resulting password to the console
print("Password:", password)
print()
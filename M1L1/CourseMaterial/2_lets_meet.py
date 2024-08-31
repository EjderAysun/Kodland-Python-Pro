# Let's Meet!
print()
#----------
# Python Basics

# What will be the output of this program?
my_words = ["Hi!", "Python Pro", "Kodland"]
print(my_words[1])
# Output: Python Pro

# What will this code do?
# The parameter of the input method can be left empty.
name = input()  # name = isim
print("Hi ", name)
# Bu kod kullanıcıdan bir isim aldıktan sonra ona 'Hi name" şeklinde cevap verecek.

# And what's going on in this program?
import random
emojis = ["^^", "0_o", ":)", "¯\\_(ツ)_/¯", "(￢_￢)"]
print(random.choice(emojis))
'''
In this program, the library named "random" is imported.
Then a list of emoji named "emojis" is defined.
The "choice" method in the random library is used to select a random emoji from the emojis list.
The choice method takes the emojis list as a parameter.
The returned result is printed directly using the "print" keyword without passing it to a variable.
'''
print()
#----------
# Time to practice!

# Write a program that will reveal a random fact about yourself!

# [ENG]         my favorite hobby  my name  my favorite project      my favorite color
facts_about_me = ["writing code", "Ejder", "my simulation project", "black"]

'''
The "random" library can help us to select random information from the library.
Since we imported the random library above, we don't need to import it again.
'''

# Make the program print random fact.
print(random.choice(facts_about_me))
print()
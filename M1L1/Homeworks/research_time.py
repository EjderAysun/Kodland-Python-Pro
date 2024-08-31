# Research Time!
#---------- 
# Project research!
# Examine the project and try to answer the following questions:
# https://github.com/GitKodland/Translator-tur

import random

eng_words = ['Hi','Bye','Task', 'Program']
tr_words = ['Merhaba','Hoşça kalın','Görev', 'Program']
score = 0
mode = input("Select a mode: 0 for adding new words, 1 for translating: \n")

while ((mode != '0') and (mode != '1')):
    mode = input("Invalid symbol! Just type 0 or 1 (0 to add new words, 1 to translate) \n")

if mode == "1":
    print("Translate as many words as you can! You've got 10 chances!")
    for i in range(10):
        number = random.randint(0, len(eng_words)-1)  # rand = random, len = length
        print("This is how it should be translated: " + eng_words[number])
        if input() == tr_words[number]:
            print("Great!!!")
            score += 1
        else:
            print("There is a mistake... The correct word is - " + eng_words[number])
else:
    word = input("Write a word in English: ")
    translate = input("Write the translation of the word: ")
    if len(word) > 0 and len(translate) > 0:
        eng_words.append(word)
        tr_words.append(translate)
        print("Word successfully added!")

'''
Questions:

---Q1: What does the project do in general?---

The project has 2 modes:

In '0' mode the user adds a new word to the English dictionary and its translation to the Turkish dictionary.
In '1' mode, the user tries to correctly estimate the meaning of random words drawn 10 times in a row from the English dictionary.
After each word is drawn, the user writes their guess on the terminal.
If he/she gets it right, his/her score increases by 1 point and if not, his/her score does not change.

---Q2: What variables are used in the project and why?---

Variable name
eng_words     => It is used in list form to hold English words.
tr_words      => It is used in list form to hold Turkish words.
score         => It is used in integer form to keep the user's score.
mode          => It is used in string form to hold the user's selected mode.
number        => It is used in integer form to select a random integer between the first index and the last index (including both) of the 'eng_words' list.
word          => It is used in string form to hold the English word entered by the user.
translate     => It is used in string form to keep the Turkish translation of the English word entered by the user.

---Q3: What type of loop is used in this program and why?---

Loop name
while         It checks whether the 'mode' variable is entered as '0' or '1'.
              If a different string is assigned to the 'mode' variable, it gives the user an invalid symbol warning and asks the user to enter the 'mode' variable again.
              If the 'mode' variable is entered as '0' or '1', the code under the while block does not run and the program continues.

for           Since the user is allowed to guess 10 words, a for loop is used to create a fixed loop.
              In the loop, 'i' takes all integer values in the range 0-9 (including both) and then the loop ends.

---Line by Line Detailed Description---
Line
 7   - The 'random' library is imported for use in the project.
 9   - A list named 'eng_words' is created.
 10   - A list named 'tr_words' is created.
 11   - The variable 'score' is initialized by assigning 0 to it.
 12  - The 'mode' variable is created for the user to select the mode,
      the user is told to choose either '0' or '1' mode,
      the mode the user selects is assigned to the 'mode' variable.
 14  - If the 'mode' variable is not equal to '0' or '1' the code block below the while loop is executed.
 15  - The user is informed that the symbol is invalid and is prompted to re-enter the mode variable as '0' or '1'.
 17  - If the value of the mode variable is '1', the code block below the if condition is executed.
 18  - The user is informed that they have 10 chances.
 19  - A for loop is created from 0 to 10 (not including 10).
 20  - A random index is chosen between the first index and the last index (including both) of the list 'eng_words' and this index is assigned to the variable 'number'.
      randint() function is used to select a random index from the specified range (including min and max value).
 21  - The user is told which word is to be translated.
 22  - After getting the translation estimate with the input() method, it is checked directly to see if it is equal to the correct translation.
      If the estimation is correct, the code below the if block is executed.
 23  - A greeting message is printed for the user.
 24  - 1 point is added to the variable 'score'.
 25  - If the code under the if block is not executed, the code block under this block is executed.
 26  - The user is notified of the incorrect estimation and the correct translation is printed.
 27  - If the code block under the if block in the previous if block in the same indentation is not executed, the code block under this block is executed.
 28  - The English word to be inserted is retrieved from the user and assigned to the variable 'word'.
 29  - The translation of the word stored in the 'word' variable is retrieved from the user and assigned to the 'translate' variable.
 30  - If the length of the 'word' and 'translate' variables is greater than zero, i.e. if the user has not assigned empty data to these variables, the code below the if block is executed.
 31  - The variable 'word' is assigned to the list 'eng_words'.
 32  - The variable 'translate' is added to the list 'tr_words' (words with the same index are translations of each other).
 33  - The user is notified that the word and its translation have been added successfully.
 '''
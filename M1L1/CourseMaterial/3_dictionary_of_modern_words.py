# Dictionary of Modern Words
print()
#----------
# How do we store words and their meanings? What kind of variable will help us?
meme_dict = {  # dict = dictionary
            "CRINGE": "Something strange or embarrassing",
            "LOL": "A response to something funny",
            }
'''
We can store words and their meanings using a dictionary structure.
In a dictionary structure, each element consists of a key and a value.
So the dictionary stores key-value pairs.
This is a very convenient structure for storing a word and its meaning.
'''
# How do we get the user's request?
print("Welcome! You can use this app to learn the meanings of meme words.")
word = input("Write a word you don't understand (all in capital letters!): ")

# How do we process the user's request and return the description?
if word in meme_dict.keys():
    '''
    What should we do if the "word" matches?
    If the word matches, we should print the meaning of the word.
    '''
    print("The meaning of the word you are looking for: " + meme_dict[word])
else:
    '''
    What should we do if the word does not match?
    If the word does not match, we should print a message about it.
    '''
    print("The word you are looking for is not in the dictionary.")
print()
#---------- 
# How can we make the app even better?

# By adding more words to the dictionary!
meme_dict["SHEESH"] = "Disapproval"

# By looping the program to ask for 5 words at a time!
for i in range(5):
    word = input("Write a word you don't understand (all in capital letters!): ")
    if word in meme_dict.keys():
        print("The meaning of the word you are looking for: " + meme_dict[word])
    else:
        print("The word you are looking for is not in the dictionary.")
    print()

# By adding a greeting and some instructions! (Added above)
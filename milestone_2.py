# %%
import random
# %%
word_list = ["banana", "cherry", "peach","grape","persimmon"] 
word = random.choice(word_list)
# %%
# show the output of random word from the word_list
print(word)
# %%
#ask the user to enter one letter (input function)
user_input=input('Enter 1 letter as your guess: ')
guess = user_input
# %%
if len(user_input) == 1:
    print("Good guess")
else: 
    print("Oops! That is not a valid input.")
    
# %%

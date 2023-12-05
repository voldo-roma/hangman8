# %%
while True:
    guess = input("Guess a letter: ")
    #check if the guess is a single alphabetical character
    if guess.isalpha() and len(guess) == 1:
        print("Good guess")
        # in this instance, if the guess is valid, we need to break
        break
    else:
        # if the guess is invalid, e.g 78 or &, say it's invalid
        print("Invalid letter. Please, enter a single alphabetical character.")
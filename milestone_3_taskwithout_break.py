# %%
secret_word = "aicore" 
while True:
    #ask user to guess the letter
    guess = input("Guess a letter: ")
    #check if the guess is a single alphabetical character
    if guess.isalpha() and len(guess) == 1:
        print("Good guess")
        # if the guess is in the word
        if guess in secret_word:
            # Inform the user of a correct guess
            print(f"Good guess! {guess} is in the word.")
            # if I break, it shuts it down, leaving for testing
        else:
            # Step 3: Inform the user if the guess is not in the word
            print(f"Sorry, {guess} is not in the word. Try again.")
    else:
        print("Invalid letter. Please, enter a single alphabetical character.")
# %%
def guess_letter(guess, secret_word):
    guess = guess.lower()  # Convert to lower case
    if guess in secret_word:
        # tell the user of a correct guess
        print(f"Good guess! {guess} is in the word.")
        # if I break, it shuts it down, leaving for testing
    else:
        # tell the user if the guess is not in the word
        print(f"Sorry, {guess} is not in the word. Try again.")    
def ask_for_input(secret_word):
    while True:
        guess = input("Guess a letter: ")
        #check if the guess is a single alphabetical character
        if guess.isalpha() and len(guess) == 1:
            print("Good guess")
            # if the guess is in the word
            guess_letter(guess, secret_word)
        else:
            print("Invalid letter. Please, enter a single alphabetical character.")
secret_word = "aicore"
ask_for_input(secret_word)
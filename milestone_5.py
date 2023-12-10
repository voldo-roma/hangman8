# milestone_5.py
#%% 
import random
#%%

class Hangman:
    def __init__(self, word_list, num_lives=5):
        self.word_list = word_list
        self.num_lives = num_lives
        self.word = self.pick_random_word()
        self.word_guessed = ['_' for _ in self.word]
        self.num_letters = len(set(self.word))
        self.list_of_guesses = []

    def pick_random_word(self):
        return random.choice(self.word_list)

    def guess_letter(self, guess):
        guess = guess.lower()
        if guess in self.list_of_guesses:
            print(f"You already guessed '{guess}'. Try again.")
            return

        self.list_of_guesses.append(guess)

        if guess in self.word:
            for i in range(len(self.word)):
                if self.word[i] == guess:
                    self.word_guessed[i] = guess
                    self.num_letters -= 1
            print(f"Good guess! '{guess}' is in the word.")
        else:
            self.num_lives -= 1
            print(f"Sorry, '{guess}' is not in the word.")
            print(f"You have {self.num_lives} lives left.")
        
        print(f"Word: {self.display_word()}")  # Display the word with guessed letters

        if self.num_letters == 0:
            print("Congratulations! You guessed the word.")
            
    def is_game_over(self):
        return self.num_lives == 0 or ''.join(self.word_guessed) == self.word

    def display_word(self):
        return ' '.join(self.word_guessed)

    def check_guess(self, guess):
        guess = guess.lower()
        if guess in self.word:
            print(f"Good guess! '{guess}' is in the word.")
            for i in range(len(self.word)):
                if self.word[i] == guess:
                    self.word_guessed[i] = guess
                    self.num_letters -= 1
        else:
            self.num_lives -= 1
            print(f"Sorry, '{guess}' is not in the word.")
            print(f"You have {self.num_lives} lives left.")
        
        print(f"Word: {self.display_word()}")  # Display the word with guessed letters

    def ask_for_input(self):
        while True:
            guess = input("Guess a letter or the full word: ").lower()
            
            if len(guess) == 1 and guess.isalpha() and guess not in self.list_of_guesses:
                self.check_guess(guess)
                self.list_of_guesses.append(guess)
            elif len(guess) == len(self.word) and guess.isalpha():
                if guess == self.word:
                    self.word_guessed = list(self.word)
                    break
                else:
                    print(f"Sorry, '{guess}' is not the correct word.")
            else:
                print("Invalid input. Please enter a single alphabetical character or the full word.")

# Usage example:
if __name__ == "__main__":
    word_list = ["aicore", "python", "hangman"]
    game = Hangman(word_list)
    
    print("Welcome to Hangman!")
    print(f"Word: {game.display_word()}")
    
    while not game.is_game_over():
        game.ask_for_input()
    
    if ''.join(game.word_guessed) == game.word:
        print("Congratulations! You guessed the word.")
    else:
        print(f"Game over. The word was '{game.word}'. Better luck next time!")
def play_game(word_list):
    game = Hangman(word_list)
    print("Welcome to Hangman!")
    print(f"Word: {game.display_word()}")
    
    while not game.is_game_over():
        game.ask_for_input()
    
    if ''.join(game.word_guessed) == game.word:
        print("Congratulations! You guessed the word.")
    else:
        print(f"Game over. The word was '{game.word}'. Better luck next time!")
## this should call the play_game
if __name__ == "__main__":
    word_list = ["aicore", "python", "hangman"]
    play_game(word_list)
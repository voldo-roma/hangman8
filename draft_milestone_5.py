# This is the final task for Hangman project which combines all milestone tasks into one and improves the code to meet the pass criteria
# %%
import random

## Hangman class is created - the core of the game is here
class Hangman:
    def __init__(self, word_list, num_lives=5):
        self.word_list = word_list
        self.num_lives = num_lives
        self.word = self.pick_random_word()
        self.word_guessed = ['_' for _ in self.word]
        self.num_letters = len(set(self.word))
        #capture every guess in a list
        self.list_of_guesses = []
# random word is picked from the given list (see below under word_list) 
    def pick_random_word(self):
        return random.choice(self.word_list)
    #we need a function for guessing letters. 
    def guess_letter(self, guess):
        guess = guess.lower()
        if guess in self.list_of_guesses:
            print(f"You already guessed '{guess}'. Try again.")
            return

        self.list_of_guesses.append(guess)
        if guess in self.word:
            print(f"Good guess! '{guess}' is in the word.")
            for i, letter in enumerate(self.word):
                if letter == guess:
                    self.word_guessed[i] = guess
            self.num_letters = len([letter for letter in set(self.word) if letter not in self.word_guessed])
        else:
            self.num_lives -= 1
            print(f"Sorry, '{guess}' is not in the word. You have {self.num_lives} lives left.")

        print(f"Word: {self.display_word()}")

        if self.num_letters == 0:
            print("Congratulations! You guessed the word.")
        elif self.num_lives <= 0:
            print("'You Died' [Cue the Dark Souls music]")

    def is_game_over(self):
        return self.num_lives <= 0 or ''.join(self.word_guessed) == self.word

    def display_word(self):
        return ' '.join(self.word_guessed)
    #we need another function for guessing the full word and inform user to try full word matching the number of letters or single characters only
    def ask_for_input(self):
        while True:
            guess = input("Guess a letter or the full word: ").lower()
            if not guess.isalpha():
                print("Invalid input. Please enter a single alphabetical character or the full word.")
            elif guess in self.list_of_guesses:
                print(f"Hey! You already guessed '{guess}'. Try again.")
            elif len(guess) == len(self.word) and guess != self.word:
                print(f"Sorry, '{guess}' is not the correct word.")
                self.num_lives -= 1
                if self.num_lives <= 0:
                    print("Game Over! No more lives left.")
                    break
            elif len(guess) == len(self.word) and guess == self.word:
                self.word_guessed = list(self.word)
                print("Congratulations! You guessed the word.")
                break
            else:
                self.guess_letter(guess)
                break
# now play_game function takes a random word, creates a Hangman object and outputs the word hidden from the player. 
# the game will continue until the player guesses the letters correctly with 5 lives to spare or the full word is guessed correctly
# Once the game is over, player gets a message and starts a new game ("Welcome to Hangman" message)
def play_game(word_list):
    game = Hangman(word_list)
    print("Welcome to Hangman!")
    print(f"Word: {game.display_word()}")

    while not game.is_game_over():
        game.ask_for_input()

    if ''.join(game.word_guessed) == game.word:
        print("Well done!")
    else:
        print(f"Game over. The word was '{game.word}'. Better luck next time!")

## this should call the play_game


if __name__ == "__main__":
    word_list = ["me","you","jazz","zelda","Manchester"]
    play_game(word_list)
# %%

#%%
#%%
import random

class Hangman:
    def __init__(self, word_list, num_lives=5):
        self.word_list = word_list
        self.num_lives = num_lives
        self.word = random.choice(self.word_list)
        self.word_guessed = ['_' for _ in self.word]
        self.num_letters = len(set(self.word))
        self.list_of_guesses = []
        print(f"The mystery word has {len(self.word)} characters")
        print(" ".join(self.word_guessed))

    def check_letter(self, letter):
        letter = letter.lower()
        if letter in self.list_of_guesses:
            print(f"{letter} was already tried.")
            return
        self.list_of_guesses.append(letter)
        if letter in self.word:
            print(f"Good guess! '{letter}' is in the word.")
            for i in range(len(self.word)):
                if self.word[i] == letter:
                    self.word_guessed[i] = letter
            self.num_letters = len(set(self.word) - set(self.word_guessed))
        else:
            self.num_lives -= 1
            print(f"Sorry, '{letter}' is not in the word. You have {self.num_lives} lives left.")
        print(" ".join(self.word_guessed))

    def ask_letter(self):
        while True:
            letter = input("Guess a letter: ")
            if len(letter) != 1 or not letter.isalpha():
                print("Please, enter just one character")
            elif letter.lower() in self.list_of_guesses:
                print(f"{letter} was already tried.")
            else:
                self.check_letter(letter)
                break

    def is_game_over(self):
        return self.num_lives <= 0 or '_' not in self.word_guessed

def play_game(word_list):
    game = Hangman(word_list)
    while not game.is_game_over():
        game.ask_letter()

    if '_' not in game.word_guessed:
        print("Congratulations! You won!")
    else:
        print(f"You lost! The word was {game.word}")

if __name__ == '__main__':
    word_list = ['apple', 'banana', 'orange', 'pear', 'strawberry', 'watermelon','me','you','zelda']
    play_game(word_list)

# %%

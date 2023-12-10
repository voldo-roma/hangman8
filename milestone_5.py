#%%
#Milestone 5 for AiCore code review
import random
# main class - core of the project
class Hangman:
    # Parameters. 
    # Word_list - possible words that get randomised; num_lives - number of guesses allowed (set at 5 as per instructions)
    def __init__(self, word_list, num_lives=5):
        self.word_list = word_list #check below for given list
        self.num_lives = num_lives #number of incorrect letter guesses allowed
        self.word = random.choice(self.word_list) #gets a random word from the word list
        self.word_guessed = ['_' for _ in self.word] #creates underscores instead of letters to aid the game
        self.num_letters = len(set(self.word)) #count letters
        self.list_of_guesses = [] #creates a list to populate with all the guess user makes
        print(f"The mystery word has {len(self.word)} characters") # first message to the user
        print(" ".join(self.word_guessed)) 
#main part - checking if letter is in word - parameter is letter
    def check_letter(self, letter):
        letter = letter.lower() # turn lowercase
        if letter in self.list_of_guesses: #checks if letter has already been used
            print(f"{letter} was already tried.") 
            return
        self.list_of_guesses.append(letter) #add to list of guesses
        #now check if letter is in the word and update guessed words
        if letter in self.word:
            print(f"Good guess! '{letter}' is in the word.")
            for i in range(len(self.word)):
                if self.word[i] == letter:
                    self.word_guessed[i] = letter
            self.num_letters = len(set(self.word) - set(self.word_guessed))
        else:
            #when guessed wrongly indicate this to the user - countdown of lives
            self.num_lives -= 1
            print(f"Sorry, '{letter}' is not in the word. You have {self.num_lives} lives left.")
        print(" ".join(self.word_guessed)) # show the updated mystery word and which letters have been revealed already

    #this method asks the user to guess a letter and checks if they use more than one character, and not number, or repeat the same value
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
    # method that checks if the game is still on - game over if 0, player hasn't guessed correctly yet
    def is_game_over(self):
        return self.num_lives <= 0 or '_' not in self.word_guessed
#function that starts the game continues until conditions are met

def play_game(word_list):
    game = Hangman(word_list) #list of words (added below)
    while not game.is_game_over(): 
        game.ask_letter()
    #final output of the game and message to finish it
    if '_' not in game.word_guessed:
        print("Congratulations! You won!")
    else:
        print(f"You lost! The word was {game.word}")
# list of words - include shorter ones on top of default aicore ones for testing.  
if __name__ == '__main__':
    word_list = ['apple', 'banana', 'orange', 'pear', 'strawberry', 'watermelon','me','you','zelda']
    play_game(word_list)
# %%

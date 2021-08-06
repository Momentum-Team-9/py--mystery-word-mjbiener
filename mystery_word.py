import random
import sys


with open("words.txt") as words_list:
    words = words_list.read().split()


easy_words = []
normal_words = []
hard_words = []
random_word = []
letters_guessed = []
quit_words = ["no", "No", "NO", "quit", "Quit", "QUIT", "exit", "Exit", "EXIT"]
start_words = ["Yes", "yes", "YES", "y", "Y"]


def start_game():
    while (True):
        print("\n Welcome to mystery word! \n")
        game_start_input = input("Would you like to play? Yes or No?")
    # if game_start_input == "Yes" or "yes" or "YES" or "y" or "Y":
    #     word_selection()
        if game_start_input in start_words:
            word_selection()
        elif game_start_input not in start_words:
            print("Goodbye!")
            sys.exit()


def word_selection():
    difficulty = input("\nPlease enter a difficulty level by letter: easy = e, normal = n. hard = h: ")
    if difficulty == "e":
        for word in words:
            if 4 <= len(word) <= 6:
                easy_words.append(word)
                random_word = random.choice(easy_words)
    elif difficulty == "n":
        for word in words:
            if 6 <= len(word) <= 8:
                normal_words.append(word)
                random_word = random.choice(normal_words)
    elif difficulty == "h":
        for word in words:
            if len(word) >= 8:
                hard_words.append(word)
                random_word = random.choice(hard_words)
    print(random_word)
    print(f"the mystery word has {len(random_word)} letters ")
    play_game()


def play_game():
    max_guesses = 8
    guess_count = 1
    letters_guessed = []
    user_input = input("Guess a letter: ")
    while user_input not in quit_words:
        
        if guess_count == 8:
            print("You have run out of guesses! Better luck next time.")
            user_input = input("Would you like to play again? Yes or No? ")
            while(True):
                if user_input in start_words:
                    word_selection()
                elif user_input not in start_words:
                    print("Goodbye!")
                    sys.exit()
        
        elif user_input in letters_guessed:
            print("You already guessed that letter!")
            user_input = input("Enter a different letter. ")
        
        elif user_input not in letters_guessed and user_input in random_word:
            letters_guessed.append(user_input)

            # add user_input to word tracking display

            print(f"you have {max_guesses-guess_count + 1} guesses remaining")
            user_input = input("Enter another letter. ")
        
        elif user_input not in (letters_guessed and random_word):
            guess_count +=1
            letters_guessed.append(user_input)
            print(f"you have {max_guesses-guess_count + 1} guesses remaining")
            user_input = input("Enter a different letter. ")
    print(letters_guessed)


def word_tracking():

    pass


start_game()

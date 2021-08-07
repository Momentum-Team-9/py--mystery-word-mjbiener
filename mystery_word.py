import random
import sys


with open("words.txt") as words_list:
    words_list = words_list.read().lower()
    words = words_list.split()


easy_words = []
normal_words = []
hard_words = []
letters_guessed = []
quit_words = ["no", "No", "NO", "quit", "Quit", "QUIT", "exit", "Exit", "EXIT"]
start_words = ["Yes", "yes", "YES", "y", "Y"]


def start_game():
    while (True):
        print("\n Welcome to mystery word! \n")
        game_start_input = input("Would you like to play? Yes or No?")
        if game_start_input in start_words:
            word_selection()
        elif game_start_input not in start_words:
            print("Goodbye!")
            sys.exit()


def word_selection():
    global random_word
    random_word = []
    
    difficulty = input("\nPlease enter a difficulty level by letter: easy = e, normal = n. hard = h: ").lower()
    # program in error/exception if input more than one letter or is not one of listed letters!
    # if difficulty != ("e" or "n" or "h"):
    #     print("please follow directions and enter a correct letter! ")
    #     input("\nPlease enter a difficulty level by letter: easy = e, normal = n. hard = h: ")
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
    print(f"the mystery word has {len(random_word)} letters ")
    play_game()


def play_game():
    print(random_word)
    max_guesses = 8
    guess_count = 1
    global letters_guessed
    letters_guessed = []
    progress_display = make_word(random_word, letters_guessed)
    print(progress_display)
    user_input = input("Guess a letter: ").lower()
   #need to finish handling exceptions/errors of input
    if len(user_input) > 1:
        print("Please follow the directions - Enter only one letter at a time")
        user_input = input("Guess a letter: ").lower()
        # need to finish handling exceptions/errors of input

    while user_input not in quit_words:

        if guess_count == 8:
            print("\nYou have run out of guesses! Better luck next time.")
            print(f"The mystery word was {random_word}")
            user_input = input("Would you like to play again? Yes or No? ")
            while(True):
                if user_input in start_words:
                    word_selection()
                elif user_input not in start_words:
                    print("Goodbye!")
                    sys.exit()
        elif user_input in letters_guessed:
            print("You already guessed that letter!")
            print(f"you have guessed the following letters already {letters_guessed}")
            progress_display = make_word(random_word, letters_guessed)
            print(progress_display)
            user_input = input("Enter a different letter. ").lower()
            # need to finish handling exceptions/errors of input
        elif user_input not in letters_guessed and user_input in random_word:
            letters_guessed.append(user_input)
            print(f"you have guessed the following letters already {letters_guessed}")
            progress_display = make_word(random_word, letters_guessed)
            print(progress_display)
            if "_" not in progress_display:
                print("You Win! You are a mystery word master!")
                user_input = input("Would you like to play again? Yes or No? ")
                while(True):
                    if user_input in start_words:
                        word_selection()
                    elif user_input not in start_words:
                        print("Goodbye!")
                        sys.exit()
            else:
                print(f"you have {max_guesses-guess_count + 1} guesses remaining")
                user_input = input("\nEnter another letter. ").lower()
                # need to finish handling exceptions/errors of input
        elif user_input not in (letters_guessed and random_word):
            guess_count += 1
            letters_guessed.append(user_input)
            print(f"That letter is not in the word. You have {max_guesses-guess_count + 1} guesses remaining")
            print(f"you have guessed the following letters already {letters_guessed}")
            progress_display = make_word(random_word, letters_guessed)
            print(progress_display)
            user_input = input("Enter a different letter. ").lower()
    print(letters_guessed)


def show_word(letter, guesses):
    if letter in guesses:
        return letter
    else:
        return "_"


def make_word(word, guesses):
    output_letters = [show_word(letter, letters_guessed) for letter in random_word]
    return(' '.join(output_letters))


start_game()

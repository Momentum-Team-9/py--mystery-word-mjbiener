import random
import sys
import string


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
    difficulty_levels = ["e", "n", "h"]
    difficulty = input("\nPlease enter a difficulty level by letter: easy = e, normal = n. hard = h: ").lower()

    if difficulty not in difficulty_levels:
        print("please follow directions and enter a correct letter to choose game level! ")

    if difficulty == "e":
        easy_words = [word for word in words if 4 <= len(word) <= 6]
        random_word = random.choice(easy_words)
        print(f"the mystery word has {len(random_word)} letters ")
        play_game()

    elif difficulty == "n":
        normal_words = [word for word in words if 6 <= len(word) <= 8]
        random_word = random.choice(normal_words)
        print(f"the mystery word has {len(random_word)} letters ")
        play_game()

    elif difficulty == "h":
        hard_words = [word for word in words if len(word) >= 8]
        random_word = random.choice(hard_words)
        print(f"the mystery word has {len(random_word)} letters ")
        play_game()


def play_game():
    max_guesses = 8
    guess_count = 1
    global letters_guessed
    letters_guessed = []
    string.ascii_letters
    valid_guesses = list(string.ascii_letters)
    progress_display = make_word(random_word, letters_guessed)
    print(progress_display)
    user_input = input("Guess a letter: ").lower()

    while user_input not in quit_words:

        if len(user_input) > 1 or user_input not in valid_guesses:
            print("Please follow the directions - Enter only one letter at a time")
            user_input = input("Guess a letter: ").lower()

        elif user_input not in letters_guessed and user_input in random_word:
            letters_guessed.append(user_input)
            print(f"\nGreat choice! {user_input} is in the word!")
            print(f"you have guessed the following letters already {letters_guessed}")
            progress_display = make_word(random_word, letters_guessed)
            print(progress_display)
            if "_" not in progress_display:
                print("You Win! You are a mystery word master!")
                user_input = input("\nWould you like to play again? Yes or No? ")
                while(True):
                    if user_input in start_words:
                        word_selection()
                    elif user_input not in start_words:
                        print("Goodbye!")
                        sys.exit()
            else:
                print(f"you have {max_guesses-guess_count + 1} guesses remaining")
                user_input = input("\nEnter another letter. ").lower()

        elif guess_count == max_guesses:
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

# Day 12 - Task 5 - Number Guessing Program

# Import the ASCII art for the program
import art

# Import the random module
import random

# Set LOGO to the ASCII art
LOGO = art.logo

# Set constant global variables for the number of attempts as
# the chosen difficulty level
HARD = 5
EASY = 10

# Define function to get a valid guess from user.
def get_user_guess( ):
    """ Gets a valid guess from the user.
    A valid guess must be an integer from 1 to 100, inclusive.
    It cannot be any other character(s) or types of number like a float.
    """

    # Set th user guess to 0
    guess = 0

    # Indicate that no valid user input has been found yet
    valid_guess_input = False

    # Loop while there has been no valid input from the user
    while not valid_guess_input:

        # Ask the user for a guess
        guess_input = input("Make a guess: ")

        # Indicate that the user guess is a string that can be converted into an
        # integer to begin with.
        guess_is_an_integer = True

        # Check if the user's guess can be converted to an integer
        try:

            # Try and convert to an integer
            int(guess_input)

        # Check exception type:
        except ValueError:

            # Cannot convert to an integer so indicate this
            guess_is_an_integer = False

        # Is user guess input convertible to an integer?
        if guess_is_an_integer:

            # Yes, so convert to integer
            guess = int(guess_input)

            # Is guess more than 0?
            if guess > 0:

                # Yes, is guess less 101?
                if guess < 101:

                    # Yes, indicate a valid guess
                    valid_guess_input = True

                # No, guess is more than 100
                else:

                    # Print out message to the user about their guess being too high.
                    print("You have typed invalid input. Try again. You cannot type in an integer more than 100.")

                    # Indicate an invalid guess
                    valid_guess_input = False

            # No, guess is less than 1.
            else:

                # Print out message to the user about their guess being too low.
                print("You have typed invalid input. Try again. You cannot type in an integer less than 1.")

                # Indicate an invalid guess
                valid_guess_input = False

        # No, so guess input from user cannot be an integer as astring
        else:

            # Print out message to the console that invalid character(s) or another type of number has been entered.
            print("You have typed invalid input. Try again. You cannot input any character(s) or a number that is not an integer.")

            # Indicate an invalid guess
            valid_guess_input = False

    # End of loop so return a valid integer
    return guess

# Print LOGO to the console
print(LOGO)

# Print welcome messages to the console
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100...")

# Generate a random number between 1 and 100
number = random.randint(1, 100)

# Ask the user to choose a difficulty level from 'easy' or 'hard'
difficulty_level = input("Choose a difficulty: Type 'easy' or 'hard': ")

# Loop while user is not typing in a valid difficulty level
while difficulty_level != 'easy' and difficulty_level != 'hard':

    # Print message informing user that they have made an invalid choice
    print("You have chosen an invalid difficulty level: Please try again.")

    # Ask the user to choose a difficulty level from 'easy' or 'hard'
    difficulty_level = input("Choose a difficulty level: Type 'easy' or 'hard': ")

# Set the number starting attempts to 10
attempts_remaining = EASY

# Is the chosen difficulty level equal to 'hard'?
if difficulty_level == 'hard':

    # Yes, so set it to 5 attempts
    attempts_remaining = HARD

# Print out the number of attempts that the user has
print(f"You have {attempts_remaining} attempts to guess the number:")

# Set status of the game status to game is in play
game_is_in_play = True

# Loop while game is in play
while game_is_in_play:

    # Get valid guess input from user
    user_guess = get_user_guess()

    # Is the user's guess equal to the random number?
    if user_guess == number:

        # Yes, so set the game message for the end result of the game
        # to be printed to the console.
        game_message = "Correct! You win! "

        # Are there more than one attempt remaining?
        if attempts_remaining > 1:

            # Yes, so add the number of attempts remaining to the game message.
            game_message += f"You have won the game with {attempts_remaining} attempts remaining."

        else:

            # No, so add that only one attempt remains to the game message
            game_message += f"You have won the game with {attempts_remaining} attempt remaining."

        # Print the game message to the console.
        print(game_message)

        # Set the game status to game is not in play
        game_is_in_play = False

    # No, so it must be greater than or smaller than the random number.
    else:

        # Is, the user's guess greater than the random number?
        if user_guess > number:

            # Yes, so set game message to "Too high."
            game_message = "Too high."

        # No, so it must be smaller
        else:

            # Set game message to "Too low"
            game_message = "Too low"

        # Decrement the number of attemts remaining
        attempts_remaining -= 1

        # Print the game message to the console
        print(game_message)

        # Print out how many attempts there are remaining to the console.
        print(f"You have {attempts_remaining} attempts remaining.")

        # Are there any more attempts remaining?
        if attempts_remaining == 0:

            # Print out message to say what the number was to be guessed
            print(f"You lose. The number was: {number}.")

            # No, so set the game status to game is not in play
            game_is_in_play = False

# END OF WHILE-LOOP


# Day 14 - Task 1 - Higher or Lower Program

# Import the random module
import random

# Import ASCII art for game logo
import art

# Import game data
import game_data

# Define function to compare brands
def compare_brands(brand_0, brand_1):

    # Are all key:value pairs equal?
    if brand_0['name'] == brand_1['name'] and \
       brand_0['follower_count'] == brand_1['follower_count'] and \
       brand_0['description'] == brand_1['description'] and \
       brand_0['country'] == brand_1['country']:

       # Yes, so return False
        return False

    # No
    else:

        # Return True
        return True

# Set GAME_LOGO to ASCII art for game logo
GAME_LOGO = art.logo

# Set COMPARE_LOGO to ASCII art for compare logo
COMPARE_LOGO = art.vs

# Set GAME_DATA to game data
GAME_DATA = game_data.data

# Set game data count to the number of items in game data
game_data_count = len(GAME_DATA)

# Print GAME_LOGO to the console
print(GAME_LOGO)

# Create empty dictionary for brands already selected
brands_already_selected = []

# Define and initialise loop-control variable
game_is_in_play = True

# Define and initialise user score
user_score = 0

# Define and initialise brand A profile to a random brand profile
brand_A_profile = random.choice(GAME_DATA)

# Append brand A profile to brands already selected
brands_already_selected.append(brand_A_profile)

while game_is_in_play:

    # Set already selected count to the number of items in brands already selected
    already_selected_count = len(brands_already_selected)

    # Have all brand profiles been selected from game data?
    if not already_selected_count == game_data_count:

        # No, so define and initialise brand B profile to a random brand profile
        brand_B_profile = random.choice(GAME_DATA)

        # Check if the selected brands are different
        brands_are_different = compare_brands(brand_A_profile, brand_B_profile)

        # Compare brand A profile and brand B profile to see if they are the same
        if brands_are_different :

            # They are different brands so check if brand B has already been selected
            if not brand_B_profile in brands_already_selected:

                # No, brand B profile has not already been selected. Print brand A profile details to the console
                print(f"Compare A: {brand_A_profile['name']}, a {brand_A_profile['description']} from {brand_A_profile['country']}")

                # Print compare logo to the console
                print(COMPARE_LOGO)

                # Print brand B profile details to the console
                print(f"Against B: {brand_B_profile['name']}, a {brand_B_profile['description']} from {brand_B_profile['country']}")

                # Set A follower count variable
                A_follower_count = brand_A_profile['follower_count']

                # Set B follower count variable
                B_follower_count = brand_B_profile['follower_count']

                # Ask the user who has more followers
                user_selection = input("Who has more followers?: Type 'A' or 'B': ").upper()

                # Loop while user has typed an invalid selection
                while user_selection != 'A' and user_selection != 'B':

                    # Print out message to the console telling user has typed an invalid selection
                    print("You have typed an invalid selection. Please try again.")

                    # Ask the user who has more followers
                    user_selection = input("Who has more followers?: Type 'A' or 'B': ").upper()

                # Is user selection equal to 'A'
                if user_selection == 'A':

                    # Is follower count of 'A' greater than follower count of 'B'?
                    if A_follower_count > B_follower_count:

                        # Increment user score by 1
                        user_score += 1

                        # Print a message to the console that the user is right and their score
                        print(f"You're right! Current score {user_score}")

                    # No
                    else:

                        # Check if they are not equal
                        if not A_follower_count == B_follower_count:

                            # A follower count is less than B follower count so exit the game
                            game_is_in_play = False

                # No, so user selection is 'B'
                else:

                    # Is follower count of 'B' greater than follower count of 'A'?
                    if B_follower_count > A_follower_count:

                        # Set brand A profile to brand B profile
                        brand_A_profile = brand_B_profile

                        # Increment user score by 1
                        user_score += 1

                        # Print a message to the console that the user is right and their score
                        print(f"You're right! Current score {user_score}")

                    else:

                        # Check if they are not equal
                        if not B_follower_count == A_follower_count:

                            # B follower count is less than A follower count so exit the game
                            game_is_in_play = False

    else:

        # Print message to the console saying its the end of the game
        print("End of the game. You have no more brands to compare.")

        # Indicate that game is no longer in play
        game_is_in_play = False

# END OF WHILE-LOOP

# Print message to the console saying user has guessed incorrectly and their final score
print(f"Sorry, that's wrong. Final score: {user_score}")







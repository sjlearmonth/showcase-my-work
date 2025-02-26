# Day 16 - Task 1 - OOP Version of the Coffee Machine Program

class CoffeeMachine:
    """
    Models all the functionality of a coffee machine.
    """

    def __init__(self):
        self.resources = {
            "water": 300,
            "milk": 200,
            "coffee": 100,
        }
        self.is_ON = True
        self.menu = {
            "latte" : self.ItemInfo( water=200, milk=150, coffee=24, cost=2.5 ),
            "espresso": self.ItemInfo(water=200, milk=150, coffee=24, cost=2.5),
            "cappuccino": self.ItemInfo(water=200, milk=150, coffee=24, cost=2.5)
        }

    class ItemInfo:
        """Models the information about each menu item."""

        def __init__(self, water, milk, coffee, cost):
            self.cost = cost
            self.ingredients = {
                "water": water,
                "milk": milk,
                "coffee": coffee
            }

    # Define the function to get the customer's coffee choice.
    def get_customer_coffee_choice(self):
        """
        Ask the customer for their coffee choice from "Espresso", "Latte" or "Cappuccino"
        and for input of "report" or "off".

        Also check for invalid input from the customer.

        :return: customer_choice
        """

        # Indicate that customer input is invalid at this point.
        customer_input_is_invalid = True

        # Ask the customer what coffee they would like to be served.
        customer_choice = input(
            "Espresso, Latte and Cappuccino coffees are available. What would you like to drink? ").lower()

        # Continue to loop until the customer inputs valid input.
        while customer_input_is_invalid:

            # Is customer input a valid choice.
            if customer_choice == 'espresso' or customer_choice == 'latte' or \
                    customer_choice == 'cappuccino' or customer_choice == 'report' or \
                    customer_choice == 'off':

                # Yes, so indicate valid customer input.
                customer_input_is_invalid = False

            # No, customer input is invalid.
            else:

                # Print out message to the customer saying invalid input has been entered.
                print("Error: You have typed an invalid choice. Please try again.\n")

                # Ask the customer what coffee they would like to be served.
                customer_choice = input(
                    "Espresso, Latte and Cappuccino coffees are available. What would you like to drink? ").lower()

        # Return the customer's choice.
        return customer_choice

    # Define the function to serve the customer their coffee from their choice.
    def serve_customer_coffee_choice(self, choice):
        """
        Calls check_and_update_machine_resources(...) to see if the customer's choice
        of coffee can be made and updates the machine resources accordingly.

        If the machine does not have enough resources to make their coffee then this function
        prints out what particular resource it does not have enough of and returns False,
        otherwise True is returned.

        The function also asks the customer for more coins if they have not inserted enough for that
        particular drink. It prints out any change that customer is due.

        :param choice:
        :return: drink_is_served
        """

        # Get the resources status from checking the machine's resources against the
        # customer's choice of coffee and its ingredients.
        resources_status = self.check_and_update_machine_resources(choice)

        # Get indication of customer's coffee choice can be made.
        there_are_enough_resources = resources_status["drink is available"]

        # Are there enough resources?
        if there_are_enough_resources:

            # So, fetch the cost of the coffee.
            coffee_cost = self.menu[choice].cost

            # Does the name of the coffee begin with a vowel?
            if choice[0] in ['a', 'e', 'i', 'o', 'u']:

                # Yes, so prefix coffee name with 'An '.
                coffee_cost_message_start = "An "

            # No, so prefix coffee name with "A ".
            else:

                coffee_cost_message_start = "A "

            # Print out message to the console saying how much the coffee costs.
            print(coffee_cost_message_start + f"{choice} costs $" + f"{coffee_cost:.2f}")

            # Define and initialize the amount of customer change
            customer_change = 0.00

            # Fetch the total amount tendered by the customer.
            amount_tendered = self.get_customer_coins_total()

            # Compute the change due, if any.
            customer_change = amount_tendered - coffee_cost

            # Continue to ask customer to insert more coins is he/she has not entered
            # enough for the cost of the coffee.
            while customer_change < 0.00:

                # Print error message to the customer.
                print("Error: You have not inserted enough coins.")

                # Does the customer's choice of coffee name begin with a vowel?
                if choice[0] in ['a', 'e', 'i', 'o', 'u']:

                    # Yes, so prefix coffee name with " an ".
                    customer_coffee_cost_message_start = " an "

                else:

                    # Yes, so prefix coffee name with " a ".
                    customer_coffee_cost_message_start = " a "

                # Print out message to the console saying how much extra the customer
                # needs to insert to pay for their choice of coffee.
                print(f"You need to insert another $" + f"{-customer_change:.2f} for" +
                      customer_coffee_cost_message_start + f"{choice} coffee.\n")

                # Fetch the amount tendered by the customer and add to any previous amount.
                amount_tendered += self.get_customer_coins_total()

                # Compute the change due, if any.
                customer_change = amount_tendered - coffee_cost

            # Print out message saying the customer's coffee has been served.
            print(f"Here is your {choice}! Enjoy!")

            # Does the customer have any change due?
            if customer_change > 0.00:
                # Yes, print out the change due.
                print(f"And here is $" + f"{customer_change:.2f} change.\n")

            # Indicate that the coffee has been served successfully.
            coffee_is_served = True

        # No, there is one or more resources insufficient.
        else:

            # Is there insufficient water?
            if "water" in resources_status.keys():
                # Yes, so fetch the amount of water remaining in the machine.
                water_remaining = resources_status['water']["remaining"]

                # and fetch the amount of water required to make the coffee.
                water_required = resources_status['water']["required"]

                # Print out a message to the customer saying there is not enough water
                # to make their coffee.
                print(
                    f"Your coffee needs {water_required}ml of water but the machine only has {water_remaining}ml left.")

            # Is there insufficient milk?
            if "milk" in resources_status.keys():
                # Yes, so fetch the amount of milk remaining in the machine.
                milk_remaining = resources_status['milk']["remaining"]

                # Yes, so fetch the amount of milk required in the machine.
                milk_required = resources_status['milk']["required"]

                # Print out a message to the customer saying there is not enough milk
                # to make their coffee.
                print(
                    f"Your coffee needs {milk_required}ml of milk but the machine only has {milk_remaining}ml left.")

            # Is there insufficient coffee?
            if "coffee" in resources_status.keys():
                # Yes, so fetch the amount of coffee remaining in the machine.
                coffee_remaining = resources_status['coffee']["remaining"]

                # Yes, so fetch the amount of coffee required in the machine.
                coffee_required = resources_status['coffee']["required"]

                # Print out a message to the customer saying there is not enough coffee
                # to make their coffee.
                print(
                    f"Your coffee needs {coffee_required}g of coffee but the machine only has {coffee_remaining}g left.")

            # Indicate that the coffee has not been served successfully.
            coffee_is_served = False

        # Return result of trying to serve the customer their choice of coffee.
        return coffee_is_served

    def check_and_update_machine_resources(self, choice):
        """
        Checks to see if there are enough machine resources: water, milk and coffee
        for the machine to make and serve the customer with their choice of coffee.

        Returns a dictionary indicating if there are not enough machine resources and which ones
        there are not enough of with quantities required and quantities available.
        """

        # define and initialize dictionary for resources status.
        resources_status = {"customer choice": choice}

        # Indicate that the customer's choice of coffee is available.
        coffee_is_available = True

        # Fetch the amount of water remaining.
        water_remaining = self.resources["water"]

        # Fetch the amount of milk remaining.
        milk_remaining = self.resources["milk"]

        # Fetch the amount of coffee remaining.
        coffee_remaining = self.resources["coffee"]

        # Fetch the ingredients for the customer's choice of coffee.
        choice_ingredients = self.menu[choice].ingredients

        # Fetch the required amount of water for the customer's coffee.
        water_required = choice_ingredients["water"]

        # customer try-except block to fetch the required amount of milk
        # as the coffee may be an espresso that needs no milk.
        try:

            # Fetch the required amount of milk.
            milk_required = choice_ingredients["milk"]

        # Catch the error condition if the milk ingredient does not exist for espresso in
        # choice ingredients dictionary.
        except KeyError:

            # Set the amount of milk required to 0ml.
            milk_required = 0

        # Fetch the required amount of coffee for the customer's coffee.
        coffee_required = choice_ingredients["coffee"]

        # Is there enough water for this coffee?
        if water_required > water_remaining:
            # No, so indicate that this coffee is not available.
            coffee_is_available = False

            # Save the required and remaining amount of water.
            resources_status["water"] = {"required": water_required, "remaining": water_remaining}

        # Is there enough milk for this coffee?
        if milk_required > milk_remaining:
            # No, so indicate that this coffee is not available.
            coffee_is_available = False

            # Save the required and remaining amount of milk.
            resources_status["milk"] = {"required": milk_required, "remaining": milk_remaining}

        # Is there enough coffee for this coffee?
        if coffee_required > coffee_remaining:
            # No, so indicate that this coffee is not available.
            coffee_is_available = False

            # Save the required and remaining amount of coffee.
            resources_status["coffee"] = {"required": coffee_required, "remaining": coffee_remaining}

        # Is this coffee available to be made
        if coffee_is_available:
            # Save the required and remaining amount of water.
            water_remaining = water_remaining - water_required

            # Save the required and remaining amount of milk.
            milk_remaining = milk_remaining - milk_required

            # Save the required and remaining amount of coffee.
            coffee_remaining = coffee_remaining - coffee_required

            # Update machine resources dictionary with the amount of water remaining.
            self.resources['water'] = water_remaining

            # Update machine resources dictionary with the amount of milk remaining.
            self.resources['milk'] = milk_remaining

            # Update machine resources dictionary with the amount of coffee remaining.
            self.resources['coffee'] = coffee_remaining

        # Indicate the status of coffee availability
        resources_status["drink is available"] = coffee_is_available

        # Return the resources status dictionary
        return resources_status

    # Define a function to fetch the customer's coins.
    def get_customer_coins_total(self):
        """
        Fetch the customer's coins and add up their value.

        :return: coins_total
        """

        # Define the constant for a quarter's value in dollars.
        QUARTERS_VALUE = 0.25

        # Define the constant for a dime's value in dollars.
        DIMES_VALUE = 0.10

        # Define the constant for a nickle's value in dollars.
        NICKLES_VALUE = 0.05

        # Define the constant for a penny's value in dollars.
        PENNIES_VALUE = 0.01

        # Get the number of quarters from the customer.
        quarters = self.get_valid_input('quarters')

        # Get the number of dimes from the customer.
        dimes = self.get_valid_input('dimes')

        # Get the number of nickles from the customer.
        nickles = self.get_valid_input('nickles')

        # Get the number of pennies from the customer.
        pennies = self.get_valid_input('pennies')

        # Compute the total value of all coins in dollars.
        coins_total = quarters * QUARTERS_VALUE + \
                      dimes * DIMES_VALUE + \
                      nickles * NICKLES_VALUE + \
                      pennies * PENNIES_VALUE

        # Return the total cost in dollars.
        return coins_total

    # Define function to get the quantity of the customer's coins and check for invalid input.
    def get_valid_input(self, coin_type):
        """
        Get the number of coins from the customer depending on coin type;
        quarters, dimes, nickles or pennies.

        Check for invalid input; only an integer greater than or equal to zero is allowed.
        :param coin_type:
        :return: number_of_coins
        """

        # Define and initialize number of coins inserted by the customer
        number_of_coins = 0

        # Indicate that customer input is invalid at the start
        customer_input_is_invalid = True

        # Continue to loop while customer has entered invalid input.
        while customer_input_is_invalid:

            # Use try-except block to catch error condition when customer eneters an invalid input.
            try:

                # Fetch the number of coins from the customer input./
                number_of_coins = int(input(f"Please insert number of {coin_type}: "))

                # Indicate customer has entered a valid number of coins.
                customer_input_is_an_integer = True

            # Catch the error condition.
            except ValueError:

                # Indicate customer has entered an invalid number of coins.
                customer_input_is_an_integer = False

            # Is customer input an integer?
            if customer_input_is_an_integer:

                # Yes, is number of coins greater than or equal to zero?
                if number_of_coins >= 0:

                    # Yes, so indicate the customer has entered valid input
                    customer_input_is_invalid = False

                # No, an integer less than zero has been entered.
                else:

                    # Print out error message to the console.
                    print("Error: You have entered a number of coins less than zero.")

                    print("Please try again.")

            # No, customer has not entered an integer of any value.
            else:

                # Print out error message to the console.
                print(f"Error: You cannot enter anything but an integer greater than or equal to 0.")

                print("Please try again.")

        # Return a valid number of coins
        return number_of_coins

    def get_customer_alternate_coffee_decision(self):

        alternate_coffee_decision = input("Would you like another coffee? 'y' or 'n': ")

        # Continue to loop until the user has entered 'y' or 'n'.
        while not (alternate_coffee_decision == 'y' or alternate_coffee_decision == 'n'):

            # The use has entered invalid choice.
            print("Error: You have typed an invalid choice: Please try again.")

            # Ask the user again.
            alternate_coffee_decision = input("Would you like another coffee? 'y' or 'n': ")

        return alternate_coffee_decision

    # Define function to print report of remaining coffee machine resources
    def print_report(self):

        # Calculate the amount of extra spaces needed for water quantity less than 100ml.
        water_padding = " " * (3 - len(str(self.resources['water'])))

        # Calculate the amount of extra spaces needed for milk quantity less than 100ml.
        milk_padding = " " * (3 - len(str(self.resources['milk'])))

        # Calculate the amount of extra spaces needed for coffee quantity less than 100g.
        coffee_padding = " " * (3 - len(str(self.resources['coffee'])))

        # Some indentation to make report table look pretty.
        indentation_padding = " " * 4

        # Print out the report table with the remaining resource quantities of coffee machine.
        print("\n")
        print(indentation_padding + "-" * 44)
        print(indentation_padding + "|             Resources Report             |")
        print(indentation_padding + "-" * 44)
        print(indentation_padding + "|    Machine Resources    |    Quantity    |")
        print(indentation_padding + "-" * 44)
        print(
            indentation_padding + f"|        Water            |    {self.resources['water']}ml" + water_padding + "       |")
        print(
            indentation_padding + f"|        Milk             |    {self.resources['milk']}ml" + milk_padding + "       |")
        print(
            indentation_padding + f"|        Coffee           |    {self.resources['coffee']}g" + coffee_padding + "        |")
        print(indentation_padding + "-" * 44)
        print("\n")

        return

    def print_switched_off_message(self):

        print("\n")

        print("Sorry but the coffee machine has been switched off for maintenance.")

        print("Please come again another time.")

        return


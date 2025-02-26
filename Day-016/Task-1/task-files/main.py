# Day 16 - Task 1 - OOP Version of the Coffee Machine Project

# Import coffee machine class
from coffee_machine import CoffeeMachine

# Import customer class
from customer import Customer

# Create coffee machine object from CoffeeMachine class
coffee_machine = CoffeeMachine()

# Create customer object from Customer class
customer = Customer()

# Loop until coffee machine is switched off
while coffee_machine.is_ON:

    # Fetch the user's choice of coffee drink
    customer.coffee_selected = coffee_machine.get_customer_coffee_choice()

    # Has user entered a valid coffee choice?
    if customer.coffee_selected == 'espresso' or customer.coffee_selected == 'latte' or customer.coffee_selected == 'cappuccino':

        # Indicate if the user has been successfully served with their choice of coffee.
        customer.coffee_is_served = coffee_machine.serve_customer_coffee_choice(customer.coffee_selected)

        # Has user been served successfully?
        if not customer.coffee_is_served:

            # No, so indicate coffee machine is switched off.
            coffee_machine.is_ON = False

        # Yes, so invite the user to chose another coffee.
        else:

            # Fetch user's decision to choose another coffee or not.
            customer.alternate_coffee_decision = coffee_machine.get_customer_alternate_coffee_decision()

            # Has user chosen not to choose another coffee?
            if customer.alternate_coffee_decision == 'n':

                # Yes, so indicate that the coffee machine has been switched off.
                coffee_machine.is_ON = False


    # No, has user chosen to print out report of coffee machine resources?
    elif customer.coffee_selected == 'report':

        # Yes, so print out report.
        coffee_machine.print_report()

    # No, so switch off machine
    else:

        # Yes, so indicate that the coffee machine has been switched off.
        coffee_machine.is_ON = False

##########################
# End of while-loop      #
##########################

coffee_machine.print_switched_off_message()







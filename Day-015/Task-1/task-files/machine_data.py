# Day 15 - Task 1 - Data for the coffee machine program

# Create a dictionary of dictionaries for the coffee menu choices
COFFEE_MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

# Create a dictionary of available machine resources
machine_resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

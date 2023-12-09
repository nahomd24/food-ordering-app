import random as random
# In this project i will be creating a food ordering app
# this project will demo course compentencies in python
# i will use dicts, variables, string manipulation and various other python tools


def merge(Food_list, drink_list):
    #This function will merge the food and drink dicts into a new dict called menu
    menu = Food_list.copy()
    menu.update(drink_list)
    return menu

Food_list = {
    "cheeseburger": 8.99,
    "hamburger": 7.99,
    "bacon burger": 10.99,
    "chicken sandwich": 9.99,
    "french fries": 4.99,
    "hotdog": 3.99
}

drink_list = {
    "coke": 2.99,
    "sprite": 2.99,
    "water": 1.99,
    "lemonade": 3.99,
    "milkshake": 4.99
}
#  combining the drink and food dict to create a menu
menu = merge(Food_list, drink_list)

# creating a function menu that displays the menu items
 # Program functions in Python
def display_menu():
    print("Menu:")
    for item, price in menu.items():
        print(f"{item}: ${price}")


display_menu()
# creating a variable called name 
name = input("Welcome to N and M! May I know your name for the order?")

# Asking the customer what they would like to order after viewing the menu
# using execptions to handle error 
try:
    choice = input(f"What would you like to order, {name}: ")
    if choice not in menu:
        raise ValueError("Invalid choice - item not on the menu")
    print(f"You ordered {choice}")
    print(f"{menu[choice]}")
    total_cost = menu[choice]  # Set total cost for the initial order
except ValueError as e:
    print(f"Error: {e}")
    total_cost = 0  # Set total cost to 0 for an invalid initial order
# demoing Control structures /statements
while True:
    choice = input("Would you like to order something else? (yes/no) ")

    if choice.lower() == "no":
        break
    elif choice.lower() == "yes":
        try:
            choice = input("What would you like to order: ")
            print("------------------------------")
            if choice not in menu:
                raise ValueError("Invalid choice")
            print(f"You ordered {choice}")
            print(f"{menu[choice]}")
            total_cost += menu[choice]  # Update total cost 
        except ValueError as e:
            print(f"Error: {e}")
    else:
        print("Invalid input. Please enter 'yes' or 'no'.")

if total_cost > 0:
    # using an f string to manupliate the print statement
    print(f"Thank you for your order {name} Your total cost is: ${total_cost:.2f}")
    print("--------------------------------------")
    reciept = random.randint(1, 1600)
    
else:
    print("No valid orders were placed.")

if reciept == 1560:
    print("CONGRATULATIONS YOU HAVE BEEN CHOSEN TO WIN A FREE MEAL!!!!")
    print(reciept)
else:
  print(f"your recipet number is {reciept}")

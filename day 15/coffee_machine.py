MENU = {
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

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

# checks whether resources are shortage and prints false if shortage
def enough_resources(drink):
    ingredients = MENU[drink]["ingredients"]
    for ingredient in ingredients:
        if ingredients[ingredient] <= resources[ingredient]:
            pass
        else:
            print(f"{ingredient} is in shortage")
            return False

# coin processing - Ask for coins.
## Calculate inserted money.
## Check if payment is enough.
## Return True or False.
## Tell the user the change (if any).
def coin_processing(drink):
    quarters = int(input("enter the no of quarters you inserted: "))
    quarters_value = quarters * 0.25
    dimes = int(input("enter the no of dimes you inserted: "))
    dimes_value = dimes* 0.10
    nickles = int(input("enter the no of nickles you inserted: "))
    nickles_value = nickles*0.05
    pennies = int(input("enter the no of pennies you inserted: "))
    pennies_value = pennies*0.01
    inserted_money = quarters_value + dimes_value + nickles_value + pennies_value


    drink_cost = MENU[drink]["cost"]
    if inserted_money <drink_cost:
        print("Sorry that's not enough money. Money refunded.")
        return False
    elif inserted_money == drink_cost:
        print("payment successful")
        return True
    else:
        change = inserted_money - drink_cost
        print(f"here is the {change} remaining ")
        return True

# make coffee- deduct ingredients and serve customer
def make_coffee(drink):
    ingredients = MENU[drink]["ingredients"]
    for ingredient in ingredients:
        resources[ingredient] -= MENU[drink]["ingredients"][ingredient]
    print(f"Here is your {drink}. Enjoy!")

# print report
def print_report(resources,money):
    print(f'water:{resources["water"]}ml')
    print(f'milk:{resources["milk"]}ml')
    print(f'coffee:{resources["coffee"]}ml')

money = 0
is_on = True
while is_on:
    choice = input(" What would you like? (espresso/latte/cappuccino): ")
    if choice == "off":
        is_on = False
    elif choice == "report":
        print_report(resources,money)
    elif choice in MENU  :
        if enough_resources(choice) != False:
            if coin_processing(choice):
                money += MENU[choice]["cost"]
                make_coffee(choice)
    else:
        print("Invalid choice. Please select espresso, latte, or cappuccino.")



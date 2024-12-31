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
profit = 0

# coin_type = dict(quarter=0.25)
coin_type = {
    "quarter": 0.25,
    "dime": 0.1,
    "nickle": 0.05,
    "penny": 0.01
}


def form_report():
    print(f"Water: {resources["water"]}ml")
    print(f"Milk: {resources["milk"]}ml")
    print(f"Coffee: {resources["coffee"]}g")
    print(f"Money: ${profit}")


def is_resource_sufficient(order_ingredients):
    """Returns True when order can be made, False when ingredients are insufficient """
    is_enough = True
    for item in order_ingredients:
        if resources[item] < order_ingredients[item]:
            print(f"Sorry ordered drink has insufficient {item}")
            is_enough = False
    return is_enough


def total_coin_value(count, a_coin_type):
    """Returns Total money based on coin type"""
    return coin_type[a_coin_type] * count


def process_coins():
    """Returns Total calculated from coins inserted of different types"""
    total_money = 0
    quarter_count = int(input("How many quarters?"))
    total_money += total_coin_value(quarter_count, "quarter")
    dime_count = int(input("How many dimes?"))
    total_money += total_coin_value(dime_count, "dime")
    nickle_count = int(input("How many nickles?"))
    total_money += total_coin_value(nickle_count, "nickle")
    penny_count = int(input("How many pennies?"))
    total_money += total_coin_value(penny_count, "penny")
    # print(f"total_money = {total_money}")
    return total_money


def is_transaction_successful(money_received, drink_cost):
    """Returns True if payment is accepted, False if money is insufficient"""
    global profit
    if money_received >= drink_cost:
        change = round(money_received - drink_cost, 2)
        print(f"Here is ${change} in change.")
        profit += drink_cost
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False


def make_coffee(drink_name, order_ingredients):
    """Deduct the required ingredients from the resources."""
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {drink_name} ☕")


is_on = True
while is_on:
    # TODO: 1. Prompt user by asking "What would you like? (espresso/latte/cappuccino) :"
    req = input("What would you like? (espresso/latte/cappuccino):").lower()
    if req == "off":
        is_on = False  # to be used in a method

    elif req == "report":
        # TODO: 3. Print the report
        form_report()

    # TODO: 5. Process coins
    else:
        drink = MENU[req]
        # print(drink)
        if is_resource_sufficient(drink["ingredients"]):
            payment = process_coins()
            # TODO: 6. Check transaction successful?
            if is_transaction_successful(payment, drink["cost"]):
                # TODO: 7. Make Coffee
                make_coffee(req, drink["ingredients"])

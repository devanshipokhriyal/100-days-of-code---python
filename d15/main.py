# store={'Water':'300', 'Milk': '200', 'Coffee': '100', 'Money':'0' }
# print (store)
# def make_latte():
# milk =300
# water=200
# coffee=100
# money=0

# def total_cash(quat, dim, nick, penn ):
#     quat=float(quat*0.25)
#     dim=float(dim*0.10)
#     nick=float(nick*0.05)
#     penn=float(penn*0.01)
#     t_cash=quat+dim+nick+penn
#     return t_cash

# def latte_recipie():
#     if milk>=200 and coffee>=24 and  water>=150:
#         milk =milk-200
#         coffee = coffee-24
#         water= water-150
#         money = money+2.50
#         return "heres your order!\nhave a good day!"
        

# order=input("What would you like? (espresso/latte/cappuccino):\n").lower()
# # if order=="latte":
# #     store.update({'Water':300-10, 'Milk': 200-10, 'Coffee': 100-10, 'Money':0+50 })
# #     print(store)

# print("insert coins:\n")
# quarter=int(input("How many quarters?"))
# dime=int(input("How many dimes?"))
# nickle=int(input("How many nickles?"))
# penny=int(input("How many pennies?"))

# print(f"Total money inserted : {total_cash(quarter,dime,nickle,penny)}$")
# # if total_cash(quarter,dime,nickle,penny)>=5:
# if order =="latte":
#     # a=float(2.50)
#     if total_cash(quarter,dime,nickle,penny)>=2.50:
#         print(latte_recipie())
#         if total_cash(quarter,dime,nickle,penny)>2.50:
#             balance=round(total_cash(quarter,dime,nickle,penny)-2.50, 2)
#             print(f"Heres the remainig balance :{balance}$")
#     else:
#         print("Insufficient cash.\nReturning the money.")

# print(f"{money} {milk} {coffee} {water}")


# milk = 300
# water = 200
# coffee = 100
# money = 0

# def total_cash(quat, dim, nick, penn):
#     quat = float(quat * 0.25)
#     dim = float(dim * 0.10)
#     nick = float(nick * 0.05)
#     penn = float(penn * 0.01)
#     t_cash = quat + dim + nick + penn
#     return t_cash

# def latte_recipe():
#     global milk, coffee, water, money
#     if milk >= 200 and coffee >= 24 and water >= 150:
#         milk -= 200
#         coffee -= 24
#         water -= 150
#         money += 2.50
#         return "Here's your order!\nHave a good day!"
#     else:
#         return "Sorry, not enough ingredients for a latte."

# order = input("What would you like? (espresso/latte/cappuccino):\n").lower()

# print("Insert coins:\n")
# quarter = int(input("How many quarters?"))
# dime = int(input("How many dimes?"))
# nickel = int(input("How many nickels?"))
# penny = int(input("How many pennies?"))

# total_money_inserted = total_cash(quarter, dime, nickel, penny)
# print(f"Total money inserted: ${total_money_inserted:.2f}")

# if order == "latte":
#     if total_money_inserted >= 2.50:
#         result = latte_recipe()
#         if "balance" in result:
#             print(result)
#         else:
#             print(result)
#             balance = round(total_money_inserted - 2.50, 2)
#             print(f"Here's the remaining balance: ${balance:.2f}")
#     else:
#         print("Insufficient cash.\nReturning the money.")

# print(f"Money: ${money:.2f}, Milk: {milk}, Coffee: {coffee}, Water: {water}")
# Define initial resources
# resources = {
#     "water": 300,
#     "milk": 200,
#     "coffee": 100,
#     "money": 0.0
# }

# Define menu and prices
MENU = {
    "espresso": {"ingredients": {"water": 50, "coffee": 18}, "cost": 1.5},
    "latte": {"ingredients": {"water": 200, "milk": 150, "coffee": 24}, "cost": 2.5},
    "cappuccino": {"ingredients": {"water": 250, "milk": 100, "coffee": 24}, "cost": 3.0}
}

def print_report():
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}g")
    print(f"Money: ${resources['money']:.2f}")

def check_resources(drink):
    ingredients = MENU[drink]["ingredients"]
    for ingredient, quantity in ingredients.items():
        if resources[ingredient] < quantity:
            print(f"Sorry, not enough {ingredient}.")
            return False
    return True

def process_coins():
    print("Insert coins:")
    quarters = int(input("How many quarters? "))
    dimes = int(input("How many dimes? "))
    nickels = int(input("How many nickels? "))
    pennies = int(input("How many pennies? "))
    return quarters * 0.25 + dimes * 0.10 + nickels * 0.05 + pennies * 0.01

def make_coffee(drink):
    ingredients = MENU[drink]["ingredients"]
    for ingredient, quantity in ingredients.items():
        resources[ingredient] -= quantity
    resources["money"] += MENU[drink]["cost"]


turn_off_machine = False

while not turn_off_machine:
    user_input = input("What would you like? (espresso/latte/cappuccino): ").lower()

    if user_input == "off":
        turn_off_machine = True
    elif user_input == "report":
        print_report()
    elif user_input in MENU:
        drink = user_input
        if check_resources(drink):
            cost = MENU[drink]["cost"]
            user_money = process_coins()
            if user_money < cost:
                print("Sorry, that's not enough money. Money refunded.")
            else:
                change = user_money - cost
                if change > 0:
                    print(f"Here is ${change:.2f} in change.")
                make_coffee(drink)
                print(f"Here is your {drink}. Enjoy!")
        else:
            print("Transaction failed due to insufficient resources.")


        

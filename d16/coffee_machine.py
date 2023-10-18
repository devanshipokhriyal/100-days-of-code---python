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
    "milk": 200,
    "coffee": 100,
    "water": 300,
    
}
# print(resources["milk"], resources["coffee"], resources["water"] )
cost=0.0

def total_cash(quat, dim, nick, penn): 
    quat = float(quat * 0.25)
    dim = float(dim * 0.10)
    nick = float(nick * 0.05)
    penn = float(penn * 0.01)
    t_cash = quat + dim + nick + penn
    return t_cash

def latte_recipe():
    if resources["milk"] >= 150 and resources["coffee"] >= 24 and resources["water"] >= 200:
        global cost 
        resources["milk"] -= 200
        resources["coffee"] -= 24
        resources["water"] -= 150
        cost += 2.50
        return "Here's your order!\nHave a good day!"
    else:
        return "Sorry, not enough ingredients for a latte."
    
def espresso_recipe():
    global cost
    if resources["coffee"] >= 18 and resources["water"] >= 50:
        resources["coffee"] -= 18
        resources["water"] -= 50
        cost += 1.50
        return "Here's your order!\nHave a good day!"
    else:
        return "Sorry, not enough ingredients for a latte."

def cappuccino_recipe():
    global cost
    if resources["milk"] >= 100 and resources["coffee"] >= 24 and resources["water"] >= 250:
        resources["milk"] -= 100
        resources["coffee"] -= 24
        resources["water"] -= 250
        cost += 3.0
        return "Here's your order!\nHave a good day!"
    else:
        return "Sorry, not enough ingredients for a latte."


turn_off_machine=False
while turn_off_machine!=True:

    order = input("What would you like? (espresso/latte/cappuccino):\n").lower()
    if order=="report":
        print(f"Remaining:\nMILK: {resources['milk']}Liters\nCoffee: {resources['coffee']}grams\nWater: {resources['water']}Liters\n Cost: {cost}")
    elif order!="report":
        print("Insert coins:\n")
        quarter = int(input("How many quarters?"))
        dime = int(input("How many dimes?"))
        nickel = int(input("How many nickels?"))
        penny = int(input("How many pennies?"))
       
        total_money_inserted = float(total_cash(quarter, dime, nickel, penny))
        print(f"Total money inserted: ${total_money_inserted:.2f}")
        if order == "latte":
            if total_money_inserted >= 2.50:
                print(latte_recipe())
                if total_money_inserted > 2.50:
                    remaining_balance= total_money_inserted -2.50
                    print(f"Here's the remaining balance: {remaining_balance:.2f}$")

        elif order == "espresso":
            if total_money_inserted >= 1.5:
                print(cappuccino_recipe())
                if total_money_inserted > 1.5:
                    remaining_balance= total_money_inserted -1.5
                    print(f"Here's the remaining balance: {remaining_balance:.2f}$")

        elif order == "cappuccino":
            if total_money_inserted >= 3:
                print(espresso_recipe())
                if total_money_inserted > 3:
                    remaining_balance= total_money_inserted -3
                    print(f"Here's the remaining balance: {remaining_balance:.2f}$")
        
        elif order=="off":
            turn_off_machine=True





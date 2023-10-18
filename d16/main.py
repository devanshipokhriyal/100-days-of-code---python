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


milk = 300
water = 200
coffee = 100
money = 0

def total_cash(quat, dim, nick, penn):
    quat = float(quat * 0.25)
    dim = float(dim * 0.10)
    nick = float(nick * 0.05)
    penn = float(penn * 0.01)
    t_cash = quat + dim + nick + penn
    return t_cash

def latte_recipe():
    global milk, coffee, water, money
    if milk >= 200 and coffee >= 24 and water >= 150:
        milk -= 200
        coffee -= 24
        water -= 150
        money += 2.50
        return "Here's your order!\nHave a good day!"
    else:
        return "Sorry, not enough ingredients for a latte."

order = input("What would you like? (espresso/latte/cappuccino):\n").lower()

print("Insert coins:\n")
quarter = int(input("How many quarters?"))
dime = int(input("How many dimes?"))
nickel = int(input("How many nickels?"))
penny = int(input("How many pennies?"))

total_money_inserted = total_cash(quarter, dime, nickel, penny)
print(f"Total money inserted: ${total_money_inserted:.2f}")

if order == "latte":
    if total_money_inserted >= 2.50:
        result = latte_recipe()
        if "balance" in result:
            print(result)
        else:
            print(result)
            balance = round(total_money_inserted - 2.50, 2)
            print(f"Here's the remaining balance: ${balance:.2f}")
    else:
        print("Insufficient cash.\nReturning the money.")

print(f"Money: ${money:.2f}, Milk: {milk}, Coffee: {coffee}, Water: {water}")

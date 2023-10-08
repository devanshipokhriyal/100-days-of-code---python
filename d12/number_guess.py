import random
from art import logo

# def dificulty():
#     difficulty=input("select the difficulty- easy or hard?\n")
#     if difficulty=="hard":
#         attempts=5
#     else:
#         attempts=10
#     return attempts

number = random.randint(1, 100)
print("Welcome to the Number Guessing Game\nIm thinking of a number between 1 and 100")
# print(number)
again=True

while again!=False:

# dificulty() #attempts=10/5

    difficulty=input("Select the difficulty- easy or hard?\n")
    if difficulty=="hard":
        attempts=5
    else:
        attempts=10
    gameover=False
    while attempts!=0 and gameover!=True:
        guess=int(input("guess the number:\n ") )
        if guess>number:
            print ("too high")
        elif guess<number:
            print ("too low")
        elif guess==number:
            print ("correct")
            gameover=True    
        attempts=attempts-1
    replay=input("do you want to replay? (y/n): \n")
    if replay=="y":
        again =True
    else:
        again=False


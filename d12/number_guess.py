import random

# def con(guess, number):
#     if guess>number:
#         print ("too high")
#     if guess<number:
#         print ("too - low")
#     if guess==number:
#         print ("correct")

# def difficult():
#     difficulty=input("select the difficulty- easy or hard?")
#     if difficulty=="hard":
#         attempts=5
#     else:
#         attempts=10
#     return attempts


number = random.randint(1, 100)
print(number)
# difficult()
difficulty=input("select the difficulty- easy or hard?")
if difficulty=="hard":
     attempts=5
else:
     attempts=10
    
gameover=False

while attempts!=0 and gameover!=True:
    guess=int(input("guess the number: "))
    # int(guess)
    if guess>number:
        print ("too high")
    elif guess<number:
        print ("too - low")
    elif guess==number:
        print ("correct")
        gameover=True
    # con("guess", "number")
    attempts=attempts-1






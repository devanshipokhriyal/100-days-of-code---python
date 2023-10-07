import random

def con():
    if guess>number:
        print ("too high")
    elif guess<number:
        print ("too low")
    elif guess==number:
        print ("correct")

# def difficult():
#     difficulty=input("select the difficulty- easy or hard?")
#     if difficulty=="hard":
#         attempts=5
#     else:
#         attempts=10
#     return attempts


number = random.randint(1, 100)
# difficult()
difficulty=input("select the difficulty- easy or hard?")
if difficulty=="hard":
     attempts=5
else:
     attempts=10

while attempts!=0:
    guess=input("guess the number: ")
    con()
    attempts-=attempts






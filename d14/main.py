import random
import art
from game_data import data

def format_data(account):
    name=account["name"]
    desc=account["description"]
    country=account["country"]
    return f"Name: {name }, Discription: {desc}, Country: {country}"

    


def check(Ans,A_followers, B_followers):
    if A_followers>B_followers:
        return ans=="a"
    else:
        return ans=="b"
    # if Ans == "A":
    #     A["follower_count"]>B["follower_count"]
   

score=0
print(art.logo)
again=True
B = random.choice(data)
while again!=False:
    A=B

    B = random.choice(data)
    # B = random.choice(data)
    while A == B:
        B=random.choice(data)
    print(f"Compare A : {format_data(A)}")
    print(art.vs)
    print(f"Compare B : {format_data(B)}")

    ans=input("Who has more followers A or B?\n").lower()
    A_follower_count=A["follower_count"]
    B_follower_count=B["follower_count"]

    is_correct = check(ans, A_follower_count, B_follower_count)
    if is_correct:
        score=score+1
        print(f"correct!\nCurrent score: {score}")
        
    else:
        print(f"wrong!\nYour score is {score}")
        again=False

# if ans == "a":
#     if A["follower_count"]>B["follower_count"]:
#         print("correct!") 
#         score=score+1

#     else:
#         print(f"wrong!\n your score is {score}")
      
# if ans == "b":
#     if B["follower_count"]>A["follower_count"]:
#         print("correct!")
#         score=score+1
#     else:
#         print(f"wrong!\n your score is {score}")
        

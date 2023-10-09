import random
import art
from game_data import data

# def two():
#     A = random.choice(data)
#     B = random.choice(data)
#     if A == B:
#         B=random.choice(data)
#     A_name=A["name"]
#     A_desc=A["description"]
#     A_country=A["country"]
#     print(f"Compare A: name: {A_name } description: {A_desc} country: {A_country}")
#     print(art.vs)
#     B_name=B["name"]
#     B_desc=B["description"]
#     B_country=B["country"]
#     print(f"Against B: name: {B_name } description: {B_desc} country: {B_country}")
    


# def check(Ans):
#     if Ans == "A":
#         A["follower_count"]>B["follower_count"]
   


print(art.logo)
A = random.choice(data)
B = random.choice(data)
if A == B:
    B=random.choice(data)
A_name=A["name"]
A_desc=A["description"]
A_country=A["country"]
print(f"name: {A_name } description: {A_desc} country: {A_country}")
print(art.vs)
B_name=B["name"]
B_desc=B["description"]
B_country=B["country"]
print(f"name: {B_name } description: {B_desc} country: {B_country}")
score=0
# two()
ans=input("Who has more followers A or B?\n")

if ans == "A":
    if A["follower_count"]>B["follower_count"]:
        print("correct!")
        score=score+1

    else:
        print(f"wrong!\n your score is {score}")
      
if ans == "B":
    if B["follower_count"]>A["follower_count"]:
        print("correct!")
        score=score+1
    else:
        print(f"wrong!\n your score is {score}")
        

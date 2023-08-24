import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇


choices=[rock, paper, scissors]

u_pick= int(input("What do you choose? type '0' for Rock, '1' for Paper and '2' Scissors.\n"))
# if u_pick==0:
#  print(rock)
# elif u_pick==1:
#  print(paper)
# elif u_pick==2:
#   print(scissors)
# else:
#   print("Error.\nPick From the given choices.\n") 
print(choices[u_pick])

print("Computer's choice:\n ")


c_pick=random.randint(0,2)
print(c_pick)
print(choices[c_pick])

if u_pick==c_pick:
  print("Its a draw!\n")
elif u_pick==0 and c_pick==1:
  print("You loose. Better luck next time.")
elif u_pick==0 and c_pick==2:
  print("You win. Congratulations.")
elif u_pick==1 and c_pick==0:
 print("You win. Congratulations.")
elif u_pick==1 and c_pick==2:  
  print("You loose. Better luck next time.")
elif u_pick==2 and c_pick==0:    
  print("You loose. Better luck next time.")
else:
   print("You win. Congratulations.")
print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 

#https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload

#Write your code below this line 👇
choice1= input('Youre at a cross road. Where do you want to go? type "left" or "right"\n')
if choice1=="left":
  choice2= input('You see a lake in front of you. Are you going to "swim" to the other side or are you going to "wait"\n')
  if choice2=="wait":
    choice3=input("You see three doors appear in front of you- a Red Door, a Yellow Door and a Blue Door- which door will you enter.\n")
    if choice3=="Red" or choice3=="red":
      print("You fell into a pit of fire and burned to death.\n GAME OVER.")
    elif choice3=="blue" or choice3=="Blue":
      print("You were attaked and eaten by beasts.\n GAME OVER")
    elif choice3=="yellow" or choice3=="Yellow":
      print("Success!!! \n You found the treasure!!! \n YOU WIN")
    else:
      print("Your heart coudnt contain the adventure thrills and burst. You died because of a heart attack.\n GAME OVER.")
  else:
    print("You were attacked by a trout.\n GAME OVER")
 
else:
 print("You fell into a hole.\n GAME OVER")

# from replit import clear
#HINT: You can call clear() to clear the output in the console.
from art import logo
print(logo)
print("Welcome to the secret auction program!")
dictionary={}
other_people=False
while not other_people :
  name=input("Enter your name :\n")
  bid =input("Enter your bid $ :\n")
  dictionary[name]= bid
  people=input("Are there other users who want to bid? (yes/no)\n")
  # clear()
  if people=="no":
    other_people=True
Key_max = max(zip(dictionary.values(), dictionary.keys()))[1]  
print(f"The winner is: {Key_max}" )
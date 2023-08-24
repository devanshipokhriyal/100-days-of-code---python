# Import the random module here
import random
# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
a=len(names)-1
name= random.randint(0,a)
print(f"{names[name]} is going to buy the meal today!")
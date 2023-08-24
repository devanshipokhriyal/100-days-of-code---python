# 🚨 Don't change the code below 👇
year = int(input("Which year do you want to check? \n"))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

a = year%4
if a==0:
 if year%100 == 0:
     if year%400 ==0:
         print("Leap year.")
     else:
             print("Not leap year.")
 else:
     print("Leap year.")
else:
    print("Not leap year.")             


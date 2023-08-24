print("Welcome to the tip calculator!")
bill= float(input("What was the total bill?\n"))
tip= int(input("What percentage woult you like to tip? 10, 12 or 15\n"))
people= int(input("How many people to split the bill?\n"))
tip_percent = tip/100
total_bill= (bill*tip_percent)+bill
per_person= total_bill/people
result=round(per_person,2)
print(f"Each person should pay {result}")
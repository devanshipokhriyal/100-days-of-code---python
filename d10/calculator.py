# add
def add(n1,n2):
  return n1+n2
# subtract
def sub(n1,n2):
  return n1-n2
# multiply
def mul(n1, n2):
  return n1*n2
# Division
def div(n1,n2):
  return n1/n2

# dictionary
operations={
  "+": add,
  "-": sub,
  "*": mul,
  "/":div}

num1=int(input("Enter the first number: \n"))


for symbol in operations:
  print(symbol)
should_continue=True
while should_continue:
 
  operation_symbol=input("Enter the operation to be performed:\n")
  num2=int(input("Enter the next number: \n"))
  
  calculation_function=  operations[operation_symbol]
  answer=(calculation_function(num1,num2))
  print(f"{num1} {operation_symbol} {num2} = {answer}")
  
  if input("Do you want to continue with this answer? (y/n) \n")=="y":
    num1=answer
    # num2=int(input("Enter the next number: \n"))
  else:
    should_continue=False
  


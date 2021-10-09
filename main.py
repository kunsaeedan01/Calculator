from art import logo

print(logo)

def add(num1, num2):
  return num1 + num2

def substract(num1, num2):
  return num1-num2

def multiply(num1, num2):
  return num1 * num2

def divide(num1, num2):
  return num1 /  num2

operations = {
  "+":add,
  "-":substract,
  "*":multiply,
  "/":divide
}
def calculator():
  num1 = float(input("choose the number"))
  for key in operations:
    print(key)

  should_continue = True
  
  while should_continue:
    num2 = float(input("choose the next number"))
    operation_symbol = input("Choose an operation")

    calc_function = operations[operation_symbol]
    answer = calc_function(num1, num2)

    print(f"{num1} {operation_symbol} {num2} = {answer}")
    
    if input("y to continue with this number or n for restart") == "y":
      num1 = answer
    else:
      should_continue = False
      calculator()

calculator()



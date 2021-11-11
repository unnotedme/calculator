# x + y
def add(x, y):
    return x + y

# x - y
def subtract(x, y):
    return x - y

# x * y
def multiply(x, y):
    return x * y

# x / y
def divide(x, y):
    return x / y


print("select operation:")
print("1.add")
print("2.subtract")
print("3.multiply")
print("4.divide")

while True:
    # input from the user
    choice = input("enter your choice (1/2/3/4): ")

    # check if the choice is one of the four options
    if choice in ('1', '2', '3', '4'):
        num1 = float(input("enter your first number: "))
        num2 = float(input("enter your second number: "))

        if choice == '1':
            print(num1, "+", num2, "=", add(num1, num2))

        elif choice == '2':
            print(num1, "-", num2, "=", subtract(num1, num2))

        elif choice == '3':
            print(num1, "*", num2, "=", multiply(num1, num2))

        elif choice == '4':
            print(num1, "/", num2, "=", divide(num1, num2))
        
        # check if user wants another calculation
        # break the while loop if the answer is no
        next_calculation = input("let's do more calculutions? (yes/no): ")
        if next_calculation == "no":
          break
    
    else:
        print("invalid input")
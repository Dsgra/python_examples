# First Development of simpke command-base calculator

# Create Function to define addition 
def add(x, y):
    return x + y
# Create Function to define substraction
def subtract(x, y):
    return x - y

# Create Function for multiplication
def multiply(x, y):
    return x * y

# Create Function for division
def divide(x, y):
    return x / y

# Create a display menu for operations
print("Select the Operation you want to Calculate")
print("Press: 1 to Add")
print("Press: 2 to Substract")
print("Press: 3 to Multiply")
print("Press: 4 to Division")

# Create Input to be inserted by the user
choice = input("Enter Number Choice for calculation (1/2/3/4)")
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

if choice == '1':
           print(num1,"+",num2, "=", add(num1,num2))

elif choice == '2':
           print(num1,"-",num2, "=", add(num1,num2))

elif choice == '3':
           print(num1, "*", num2, "=", multiply(num1,num2))

elif choice == '4':
           print(num1, "/", num2, "=", divide(num1,num2))
else:
           print('Invalid Input. Please Try Again')
          

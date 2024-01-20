def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Cannot divide by zero!"
    #fixed the Zero Division error and informed user that their input cannot be divided by zero
    else:
        return x / y

print("Simple Calculator")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")

#fixed invalid input occurance and added a user-friendly message
#the program doesn't run until the correct input is received
while True:
    choice = input("Select operation (1/2/3/4): ")
    if choice in ["1", "2", "3", "4"]:
        break
    else:
        print("Please enter a valid input (1, 2, 3, 4)")

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

if choice == "1":
    result = add(num1, num2)
    print(f"Result: {result}")#used f-string to correct type errors.
elif choice == "2":
    result = subtract(num1, num2)
    print(f"Result: {result}")#used f-string to correct type errors.
elif choice == "3":
    result = multiply(num1, num2)
    print(f"Result: {result}")#used f-string to correct type errors.
elif choice == "4":
    result = divide(num1, num2)
    print(f"Result: {result}")#used f-string to correct type errors.

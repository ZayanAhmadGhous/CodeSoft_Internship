# Design a simple calculator with basic arithmetic operations.Prompt the user to input two numbers and an operation choice.Perform the calculation and display the result.


print("___________________ CALCULATOR _________________________")
a=int(input("Enter first number: "))
b=int(input("Enter second number: "))

print("=="*30)

print("+ for addition")
print("- for subtraction")
print("* for multiplication")
print("/ for division")
print("% for modulus")

print("=="*30)

choice = input("Choose an operation from above: ")
if choice == '+':
    print(f'The sum of two numbres is: {a+b}')
elif choice == '-':
    print(f'The subtraction of two numbres is: {a-b}')
elif choice == '*':
    print(f'The product of two numbres is: {a*b}')
elif choice == '/':
    try:
        print(f'The qoutient of two numbres is: {a/b}')
    except:
        print("The division of any number with 0 is infinite")
elif choice == '%':
    print(f'The modulus of two numbres is: {a%b}')
else:
    print("Invalid Input")

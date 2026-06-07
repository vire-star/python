age=25

if age>=18:
    print("You are an adult.")
else:
    print("You are not an adult.")


# calculator

num1=float(input("Enter first number: "))
num2=float(input("Enter second number: "))
operator = input("Enter operator (+, -, *, /): ")


if operator == "+":
    result = num1 + num2
    print(f"{num1} + {num2} = {result}")

else:
    print("Invalid operator. Please use +, -, *, or /.")

    
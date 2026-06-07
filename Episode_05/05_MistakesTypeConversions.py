# mistake 1
# galat
# print(int("abc"))  # ValueError: invalid literal for int() with base 10: 'abc'
# print(int("3.14"))  # ValueError: invalid literal for int() with base 10: '3.14'

print(int(float("3.14")))  # sahi tarika: pehle float banao, phir int

# mistake 2

# num1 = input("Enter first number: ")
# num2  = input("Enter second number: ")

# print(num1 + num2)  # galat: ye string concatenation karega, addition nahi

# num1_int= int(num1)
# num2_int=int(num2)
# print(num1_int+num2_int)  # sahi tarika: pehle int banao, phir add karo


# mistake 3

# galat
price="99.99"
# print(int(price))  # ValueError: invalid literal for int() with base 10: '99.99'

price_float = float(price)
print(int(price_float))
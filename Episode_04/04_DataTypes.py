# Data types - python mai data kitne type ko ho sakta hai woh yeh define kartey hain

# python k data types
# 1 Numeric data types- int, float, complex
# 2 Text data type- str
# 3 Boolean data type- bool(True, False)
# 4 Sequence data types- list, tuple, range
# 5 Mapping data type- dict
# 6 Set data type- set, frozenset
# 7 None data type- NoneType


age=20
marks=100
negative_marks=-10
print(type(age))


# integer operations

print(age+5) # addition
print(age-5) # subtraction
print(age*5) # multiplication
print(age/5) # division
print(age//5) # floor division
print(age%3) # modulus
print(age**2) # exponentiation

# yeh // aur % placement mai bohot aatey hain. // floor division hota hai aur % modulus hota hai.

# float decimal numbers ko represent karta hai. int se zyada precision hota hai float mai.

price=99.99
print(type(price))

print(0.1+0.2)


# string data type- str

name="John Doe"
address='123 Main Street'
print(type(name))
print(type(address))


# string operations
print(len(name)) # length of the string
print(name.upper()) # convert to uppercase
print(name.lower()) # convert to lowercase
print(name[0]) # first character
print(name[1:4]) # substring from index 1 to 3
print(name[-1]) # last character

# f-string- formatted string literals
age=20
print(f"My age is {age}")


# Boolean data type- bool

is_passed=True
is_failed=False
print(type(is_passed))
print(type(is_failed))

# boolean operations

print(True+False) # addition
print(True*2) # multiplication
# True is treated as 1 and False is treated as 0 in arithmetic operations.

print(False*2) # multiplication
print(not True) # logical NOT
print(True or False) # logical OR

# type() function- yeh function data type ko check karne ke liye use hota hai.

# kisi bhi variable ka data type check karne ke liye hum type() function ka use karte hain.

x=10
y=3.14
z="Hello"
w=True
print(type(x)) # <class 'int'>
print(type(y)) # <class 'float'>    
print(type(z)) # <class 'str'>
print(type(w)) # <class 'bool'>
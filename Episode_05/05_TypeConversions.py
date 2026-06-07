# age = input("What is your age? ")
# next_year_age =int(age)+1
# print(next_year_age)


# explicit vs implicit type conversion

# implicit type conversion - python khud convert kar deta hai
# automatic type conversion
x=10
y=3.14
result = x+y
print(result)
print(type(result))

# explicit type conversion - programmer khud convert karta hai
age_str = "25"
age_int = int(age_str)
print(type(age_int))
print(type(age_str))

#  int() 
print(int("20"))
print(int(20.5))
print(int(True))
print(int(False))

# float banao

print(type(float("3.14")))
print(float(10))

# bool banao

print(bool(1))
print(bool("hello"))
print(bool(""))
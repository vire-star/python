text='Hello World python is great'

# case methods
print(text.upper())
print(text.lower())
print(text.title())
print(text.swapcase())


# search method
print(text.find('python'))
print(text.count('o'))
print("World" in text)
print(text.replace('python', 'java'))


# split and join
words='apple,banana,grape'
fruits = words.split(',')
print(fruits)
joined_fruits = '-'.join(fruits)
print(joined_fruits)

# f-strings
# string main varialbe daalene k teen tarike hotey hain

name = 'Alice'
age=30
marks=85

# purana tarika - concatenation
# avoid

print("my name is " +name +" and my age is " + str(age) + " and my marks are " + str(marks))


# purana tarika - format method
print("my name is {}, and my age is {}, and my marks are {}".format(name,age,marks))

# naya tarika - f-strings
print(f" my name is {name}, and my age is  {age}, and my marks are {marks}")
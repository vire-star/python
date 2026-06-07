# yeh ek concept hai jo bohot confuse karta hai beginners ko, lekin once you understand it, it will become clear.
# Immutability ka matlab hai ki once a string is created, you cannot change it.
name = 'John'
name[0]='M'  # This will raise an error because strings are immutable
print(name)  # Output: John
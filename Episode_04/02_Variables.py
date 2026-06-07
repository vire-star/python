# variable = naam -> value

player_name = "John"
player_age = 25
is_winner=True

print(player_name)
print(player_age)
print(is_winner)

# Variables Rules


name="John" # valid variable name
player_name="John" # valid variable name
playerName="John" # valid variable name
_private="hidden" # valid variable name
my_age=25 # valid variable name

# Invalid variable names
# 2name="John" # invalid variable name, cannot start with a number
# player-name=="John" # invalid variable name, cannot contain hyphens
# my age=25 # invalid variable name, cannot contain spaces
# class="match" # invalid variable name, cannot use reserved keywords

# Naming Conventions

# sname_case = Python ka standard naming convention hai. Isme words ko underscore se separate karte hain.
player_name = "John" # snake_case
student_age = 20 # snake_case
is_passed = True # snake_case

# camelCase = Isme pehla word lowercase hota hai aur baaki words ke first letter uppercase hota hai.
studentName = "Alice" # camelCase
studentAge = 20 # camelCase

# SCREAMIN_SNAKE_CASE = Isme sare letters uppercase hote hain aur words ko underscore se separate karte hain. Iska use constants ke liye hota hai.
MAX_PRICE=100
PI=3.14


# Dynamin Typing

# Python mein - types declare karne ki zarurat nahi hoti. Aap directly variable ko value assign kar sakte hain aur Python automatically uska type samajh lega.

x=10 # x is an integer
print(type(x)) # Output: <class 'int'>


b='Hello' # b is a string
print(type(b)) # Output: <class 'str'>

n=3.14 # n is a float
print(type(n)) # Output: <class 'float'>
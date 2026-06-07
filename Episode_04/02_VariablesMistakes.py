# Variables Mistakes

# Mistake 1: variable use karo define karne se pehle

# Galat
# print(age)
# age=25


# sahi
age=25
print(age)

# Mistake 2: Case sensitivity ka dhyan nahi rakhna
name="John"
Name="Alice"
NAME="Bob"
print(name)
print(Name)
print(NAME)

# python case sensitive language hai, isliye name, Name aur NAME alag alag variables hain. Agar aap case sensitivity ka dhyan nahi rakhte to aapko unexpected results mil sakte hain.


# Mistake 3: reserved keyworkd as variable name use karna
# reserved keywords wo words hote hain jo Python ke syntax ka part hote hain. Aap in keywords ko variable name ke roop mein use nahi kar sakte. Agar aap reserved keyword ko variable name ke roop mein use karte hain to aapko syntax error milega.

# Galat
class="match" # invalid variable name, cannot use reserved keywords
for=10 # invalid variable name, cannot use reserved keywords
if=5 # invalid variable name, cannot use reserved keywords
list=[1,2,3] # invalid variable name, cannot use reserved keywords

# sahi

class_name="match" # valid variable name
for_count=10 # valid variable name
if_condition=5 # valid variable name
my_list=[1,2,3] # valid variable name


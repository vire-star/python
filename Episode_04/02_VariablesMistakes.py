# Variables Mistakes ⚠️

# Mistake 1 🚫: Variable use karo define karne se pehle ❌
# Python upar se neeche code padhta hai (top to bottom)
# Agar variable define nahi kiya to usko use nahi kar sakte!

# Galat ❌
# print(age)  # ❌ ERROR! age abhi exist nahi karta!
# age=25     # Define baad mein kiya


# Sahi ✅
age=25       # Pehle define karo
print(age)   # Phir use karo - ab kaam karega! 🎯

# Yaad rakho: Define karo ➡️ Phir use karo! 🔄


# Mistake 2 🚫: Case sensitivity ka dhyan nahi rakhna ❌
name="John"
Name="Alice"
NAME="Bob"
print(name)   # Output: John
print(Name)   # Output: Alice
print(NAME)   # Output: Bob

# Sab alag alag variables hain 😲
# Python case-sensitive language hai 🐍
# isliye name, Name aur NAME teeno alag hain!
# Agar dhyan nahi rakha to unexpected results mil sakte hain 😵💫


# Mistake 3 🚫: Reserved keywords ko variable name mat do ❌
# Reserved keywords Python ke special words hote hain 
# (jaise class, for, if, list, etc.)
# Inhe variable name nahi bana sakte - syntax error aayega! 🚨

# Galat ❌
class="match"   # ❌ ERROR: 'class' reserved keyword hai
for=10          # ❌ ERROR: 'for' reserved keyword hai
if=5            # ❌ ERROR: 'if' reserved keyword hai
list=[1,2,3]    # ❌ ERROR: 'list' reserved keyword hai

# Sahi ✅ - Thoda modify karo to kaam karega!
class_name="match"  # ✅ underscore laga diya, ab valid hai!
for_count=10        # ✅ for ki jagah for_count use kiya
if_condition=5      # ✅ if ki jagah if_condition use kiya
my_list=[1,2,3]     # ✅ my_list use kiya

# 💡 Tip: Reserved keywords ki list Google pe search karlo!
# "Python reserved keywords list" - bookmark rakh lo 📑


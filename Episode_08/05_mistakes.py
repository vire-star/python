# Function Mistakes ⚠️

# Mistake 1 🚫: print() vs return() ka confusion ❌
# print() sirf screen par dikhata hai - value return nahi karta!
# return() value wapas deta hai jise aage use kar sakte ho!

# Galat ❌
# def add(a,b):
#     print(a+b)           # ❌ Sirf screen par 10 dikhayega, kuch return nahi karega!

# result = add(5,5)        # Output: 10 (screen par)
# print(result)            # Output: None (kyunki add ne kuch return nahi kiya!) 😱

# Sahi ✅
# def add(a,b):
#     return(a+b)          # ✅ return karo! Value wapas milegi!

# result = add(5,5)        # result = 10
# print(result)            # Output: 10 ✅

# 💡 Rule: print() -> sirf dikhane ke liye 🖥️
#          return() -> aage use karne ke liye 📦


# Mistake 2 🚫: Function define karne se PEHLE use karna ❌
# Python top-to-bottom execute karta hai!
# Pehle function define karo, phir call karo!

# Galat ❌
# greet("Rahul")            # ❌ ERROR! greet function abhi exist nahi karta! 🚨

# def greet(name):
#     print(f"name {name}")

# Sahi ✅ - Pehle define, phir call!
# def greet(name):
#     print(f"name {name}")

# greet("mohit")             # ✅ Ab kaam karega! Function define ho chuka hai! 🎯


# Mistake 3 🚫: return ke BAAD ka code kabhi nahi chalega ❌
# return function ko turant khatam kar deta hai!
# return ke baad jo bhi likho - woh DEAD CODE hai! ☠️

# Galat ❌
# def check(number):
#     return "positive"      # ✅ Function yahan return ho jayega
#     print("number")        # ❌ YEH KABHI NAHI CHALEGA! Return ke baad ka code! 😵

# result = check(6)
# print(result)              # Output: "positive" (print("number") kabhi execute nahi hua!)

# Sahi ✅
# def check(number):
#     return "positive"      # ✅ Sirf return karo, baaki code hata do!

# result = check(6)
# print(result)              # Output: "positive" ✅


# Mistake 4 🚫: Arguments ki sankhya galat dena ❌
# Function jitne parameters expect karta hai, utne hi arguments do!
# 2 parameters => 2 arguments! Kam/zyada mat do!

# Galat ❌
# def add(a,b):              # ✅ 2 parameters: a aur b
#     return a+b

# add(5)                     # ❌ Sirf 1 argument! TypeError: missing 1 required positional argument! 🚨
# add(5,4,6)                 # ❌ 3 arguments! TypeError: takes 2 positional arguments but 3 were given! 🚨

# Sahi ✅ - Exactly 2 arguments do!
def add(a,b):                # ✅ 2 parameters
    return a+b

result = add(5,6)            # ✅ Exactly 2 arguments! Kaam karega! 🎯
print(result)                # Output: 11 ✅

# 💡 Rule: Function(jitne parameters) = utne hi arguments do!
#          Kam arguments ❌, Zyada arguments ❌, Barabar arguments ✅
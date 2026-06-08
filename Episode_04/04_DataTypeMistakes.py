# Common mistakes with data types ⚠️

# Mistake 1 🚫: Data type mismatch ❌
# "20" yeh string hai (text), number nahi hai!
# String + integer nahi kar sakte - TypeError aayega! 🚨

# Galat ❌
# age="20"             # ❌ Yeh string hai, number nahi!
# next_year=age+1      # ❌ ERROR! String + Integer kaam nahi karega
# print(next_year)     # TypeError: can only concatenate str (not "int") to str

# Sahi ✅
age=20                 # ✅ Ab yeh integer hai (number) 🎯
next_year=age+1        # ✅ Integer + Integer = kaam karega!
print(next_year)       # Output: 21 ✅

# 💡 Yaad rakho: "" ya '' -> string, bina quotes -> number 🔢


# Mistake 2 🚫: Boolean capitalization ❌
# Python mein True/False hamesha capital T aur F se shuru hota hai!

# Galat ❌
# isvalid = true       # ❌ ERROR! Python 'true' ko nahi pehchanta
# print(isvalid)       # NameError: name 'true' is not defined 😵

# Sahi ✅
isvalid = True         # ✅ Capital T! Ab Python pehchaan lega 🎯
print(isvalid)         # Output: True ✅

# 💡 Rule: True ✅, False ✅ (capital letters!)
#          true ❌, false ❌, TRUE ❌, FALSE ❌ (yeh sab kaam nahi karenge!)


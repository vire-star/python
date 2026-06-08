# Type Conversion Mistakes ⚠️

# Mistake 1 🚫: Seedha string ko int() mein mat daalo ❌
# int() ko agar "abc" do to convert nahi kar payega - ValueError! 🚨

# Galat ❌
# print(int("abc"))      # ❌ YEH NAHI CHALEGA! 'abc' number nahi hai! 🤦
# print(int("3.14"))     # ❌ YEH BHI NAHI CHALEGA! "3.14" mein decimal hai, int seedha nahi convert karega

# Sahi ✅ - Pehle float banao, phir int!
print(int(float("3.14")))  # ✅ Pehle "3.14" -> 3.14 (float) -> phir 3 (int) 🎯
# Step by Step: "3.14" ➡️ float("3.14") = 3.14 ➡️ int(3.14) = 3 ✅


# Mistake 2 🚫: input() se jo aata hai woh STRING hota hai ❌
# input() hamesha string return karta hai!
# Agar number chahiye to pehle convert karo!

# Galat ❌
# num1 = input("Enter first number: ")   # User "5" likhega -> string "5"
# num2 = input("Enter second number: ")  # User "3" likhega -> string "3"
# print(num1 + num2)                      # ❌ Output: "53" (string concatenation!) 😱
# Yeh addition nahi karega, sirf do strings ko jod dega!

# Sahi ✅ - Pehle int banao, phir add karo!
# num1_int = int(num1)                    # ✅ "5" -> 5 (integer)
# num2_int = int(num2)                    # ✅ "3" -> 3 (integer)
# print(num1_int + num2_int)              # ✅ Output: 8 (real addition!) 🎯


# Mistake 3 🚫: Decimal wali string ko direct int() ❌
price="99.99"
# print(int(price))  # ❌ ERROR! "99.99" string hai jisme decimal hai - int() seedha nahi lega! 🚨

# Sahi ✅ - Pehle float banao!
price_float = float(price)     # ✅ "99.99" -> 99.99 (float)
print(int(price_float))        # ✅ 99.99 -> 99 (int ne decimal cut kar diya) 🎯

# 💡 Golden Rule:
# "abc" ❌ -> int() ❌ (text ko number nahi bana sakte)
# "3.14" -> float("3.14") = 3.14 ✅ -> int(3.14) = 3 ✅
# "99" -> int("99") = 99 ✅ (seedha possible!)
# "99.99" -> float("99.99") ✅ -> int() ✅ (decimal wala pehle float!)
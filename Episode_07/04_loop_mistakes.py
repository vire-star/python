# Loop Mistakes ⚠️

# Mistake 1 🚫: range() ka galat istemal ❌
# range(10) = 0 se 9 tak (10 numbers) - 1 se 10 nahi!
# Agar 1 se 10 chahiye to range(1,11) likho! 🎯

# Galat ❌
# for i in range(10):     # ❌ Output: 0,1,2,3,4,5,6,7,8,9 (1 se nahi, 0 se start!)
#     print(i)

# Sahi ✅ - Range ka sahi syntax!
# for i in range(1, 11):  # ✅ Output: 1,2,3,4,5,6,7,8,9,10 (1 se 10 tak!)
#     print(i)

# 📝 Yaad rakho: range(stop) -> 0 se stop-1 tak
#                range(start, stop) -> start se stop-1 tak
#                range(start, stop, step) -> step ke gap mein


# Mistake 2 🚫: While loop infinite (khatam nahi hota) ❌
# While loop mein condition change karna bhool gaye to
# loop kabhi nahi rukega - infinite loop! 😵💫

# Galat ❌
# i = 0
# while i < 10:
#     print(i)            # ❌ i kabhi badal nahi raha!
#                         # i hamesha 0 rahega, condition hamesha True
#                         # INFINITE LOOP! 🔁 (Ctrl+C press karo escape karne ke liye!)

# Sahi ✅ - i ko badhate raho (increment)!
i=0
while i<10:
    print(i)              # ✅ Output: 0,1,2,3,4,5,6,7,8,9
    i=i+1                 # ✅ i ko 1 se badhate raho! Loop aage badhega! 🎯

# 💡 Rule: For loop tab jab pata ho kitni baar chalana hai ✅
#          While loop tab jab sirf condition pata ho (kab tak chalana hai) ✅
#          For loop mein automatic increment hota hai, While mein khud karna padta hai! 🔄
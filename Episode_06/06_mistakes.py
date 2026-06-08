# If-Else Mistakes ⚠️

# Mistake 1 🚫: Colon (:) bhoolna ❌
# Python mein if statement ke baad colon (:) lagana zaroori hai!
# Agar colon nahi lagaya to SyntaxError! 🚨

# Galat ❌
# if age > 18              # ❌ YEH NAHI CHALEGA! Colon kahan hai? 😱
#     print("You are an adult.")  # SyntaxError: expected ':'

# Sahi ✅
# age = 20
# if age > 18:              # ✅ Colon (:) mat bhoolna! 🎯
#     print("You are an adult.")

# 💡 Rule: if, elif, else, for, while - IN SAB KE BAAD COLON LAGAO! ➡️ :


# Mistake 2 🚫: Indentation inconsistent ❌
# Python mein indentation (spaces) bahut important hai!
# Ek block ke andar sab lines ka indentation SAME hona chahiye!

# Galat ❌
# if age > 18:
#     print("adult")        # ✅ 4 spaces (sahi hai)
#   print("You can vote.")  # ❌ Sirf 2 spaces! IndentationError! 🤦
# Python confuse ho jayega - yeh if block ka hissa hai ya nahi?

# Sahi ✅ - Sab lines ka indentation SAME rakho!
# if age > 18:
#     print("adult")        # ✅ 4 spaces
#     print("You can vote.") # ✅ 4 spaces - same indentation! 🎯

# 💡 Tip: Hamesha Tab nahi, 4 spaces use karo! (Ya phir consistent raho)
# Agar Tab se shuru kiya to Tab hi use karo, spaces se to spaces hi! 🔄

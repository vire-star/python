# Common mistakes in comments 😅

# Mistake 1 🚫: Comment ko update nahi karna ❌
# Jab code change ho jaye to comment bhi change karo!
# Neeche wala comment ab galat hai kyunki code badal diya:

# Yeh comment purana hai - ab code alag hai
# x=86400
# y=x*30
# z=y*0.1

a=150  # Actually ab sirf a=150 hai, purana calculation nahi hai! ⚠️


# Mistake 2 🚫: Obvious cheeze comment karna ❌
a=15  # this is a number ❌❌ (Yeh to obvious hai, beginner bhi dekh lega 😅)

a=15 # this define user minimum age ✅✅ (Yeh batata hai ki 15 ka matlab kya hai, useful info hai! 💡)


# Mistake 3 🚫: Outdated comment ❌
# yeh function user ke age check karne ke liye hai. (Yeh to function name se hi pata chal raha hai! 🙄)
def check_age(age):
    if age>=18:
        return "You are eligible to vote."
    else:
        return "You are not eligible to vote."

# ✅ Better comment kuch aisa ho sakta tha:
# "18+ verification: returns eligibility message"
# Function ka name already "check_age" hai, 
# to comment mein wahi baat repeat mat karo! 💯
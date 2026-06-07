# commen mistakes in comment

# 1. Comment ko update nahi karna

# x=86400
# y=x*30
# z=y*0.1

a=150

# 2 obvious cheeze comment karna
a=15  # this is a number ❌❌

a=15 # this define user minimum age ✅✅



# 3. Outdated comment
# yeh function user ke age check karne ke liye hai.
def check_age(age):
    if age>=18:
        return "You are eligible to vote."
    else:
        return "You are not eligible to vote."
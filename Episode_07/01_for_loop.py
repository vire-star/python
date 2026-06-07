# loop ka matlab kya hai
# 

# i-> loop variable ya phir counter
# chaccha, doraemon, nobita, shizuka
# 0,1,2,3,4
# for i in range(5):
#     print("Hello World")

# range
# sabse important hai 
# range(stop) -> 0,1,2,3,4 this is an argument
# range(start,stop) ,range(2,5) -> 2,3,4 this is an argument


# for i in range(2,5):
#     print("Hello World")


# teen argument bhi hota hai
# range(start,stop,step) , range(2,10,2) -> 2,4,6,8 this is an argument


# for i in range(2,10,2):
#     print(i)


# native steps

# for i in range(10,2,-1):
#     print(i)


# loops k variable (i)

# i->1,2,3
# for i in range(1,11):
#     result = 2*i
#     print(f"2 x {i} = {result}")


# list k saath bhi use kar sakte hai

# names = ["chaccha", "doraemon", "nobita", "shizuka"]

# for name in names:
#     print(name)


# string k saath bhi use kar sakte hai

# name = "chaccha"
# # print(len(name))
# for letter in name:
#     print(letter)

fruits = ["apple", "banana", "cherry"]

for index,fruit in enumerate(fruits):
    print(f"{index} : {fruit}")
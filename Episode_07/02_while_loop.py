# for loop tab chalta hai jab pata ho kitni baar karna hai 
# while looop tab chalta hai jab nhi kitni bar karna hai bas ek condition chaiye

# count=0

# while count <5:
#     print("hello world")
#     count= count+1



# with user input

# correct_password = "python123"

# password =input("Enter the password: ")

# while password !=correct_password:
#     print("Incorrect password, try again.")
#     password =input("Enter the password: ")

# print("sahi password hai, welcome!")


# Break statement

# for i in range(1,11):
#     if i==5:
#         print("5 mil gaya, loop se bahar nikal raha hu")
#         break
#     print(i)

# print("Loop ke bahar aa gaya hu")

# continue statement
for i in range(1,11):
    if i%2==0:
        continue # even number ko skip karna hai
    print(i)


# break vs continue
# break-> loop poora band karo and bahar nikal jaao
# continue -> sirf bar skip karo and loop chalu rakho
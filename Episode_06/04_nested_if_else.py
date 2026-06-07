# age=int(input("Enter your age: "))
# has_id = input("Do you have an ID? (yes/no): ").lower()

# if age >=18:
#     print("You are eligible to vote.")
#     if has_id == "yes":
#         print("You can vote in the election.")
#     else:
#         print("You need an ID to vote.")
# else: 
#     print("You are not eligible to vote.")


# one liners

age=int(input("Enter your age: "))

# if age>=18:
#     print('Adult')

# else:
#     print('Minor')

print("Adult") if age>=18 else print("Minor")
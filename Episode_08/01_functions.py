# # name1="Rahul"
# # marks1=90

# # percentage1=(marks1/100)*100
# # if marks1>=90:
# #     grade1="A"
# # elif marks1>=80:
# #     grade1="B"
# # elif marks1>=70:
# #     grade1="C"
# # else:
# #     grade1="D"

# # print(f"{name1} scored {marks1} marks, which is {percentage1}%, and received grade {grade1}.")
# # name1="Payal"
# # marks1=80

# # percentage1=(marks1/100)*100
# # if marks1>=90:
# #     grade1="A"
# # elif marks1>=80:
# #     grade1="B"
# # elif marks1>=70:
# #     grade1="C"
# # else:
# #     grade1="D"

# # print(f"{name1} scored {marks1} marks, which is {percentage1}%, and received grade {grade1}.")


# def calculate_grade(name,marks):
#     percentage=(marks/100)*100
#     if marks>=90:
#         grade="A"
#     elif marks>=80:
#         grade="B"
#     elif marks>=70:
#         grade="C"
#     else:
#         grade="D"

#     print(f"{name} scored {marks} marks, which is {percentage}%, and received grade {grade}.")


# # calculate_grade()
# calculate_grade("Rahul",90)
# calculate_grade("Payal",80)

# # def -> recipe likhna
# # call -> recipe use karna

# def greet(name): # name-> parameter
#     print(f"Hello, {name}! Welcome to the world of Python programming.")

# greet("Alice") # "Alice" -> argument

# Multiple parameter


# def student_infor(name,age, city):
#     print(f"name {name}")
#     print(f"age {age}")
#     print(f"city {city}")


# student_infor("Rahul",20, "Delhi")
# student_infor("Priya",23, "Mumbai")


# Default Parameter

# def greet(name,message="How are you"):
#     print(f"Hello {name} {message}")


# greet("Rahul", "kya chal raha hai")
# greet("Priya")



# keyword Argument

# def student_info(name,age,city):
#     print(f"name {name}, age {age}, city {city}")


# # normal order se

# student_info("Rahul", 20, "delhi")

# # keyword argument

# student_info(age=20,name="Priya", city="Mumbai")




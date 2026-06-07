# like a calculator, tum usme number dete ho aur woh tumhe result deta hai, woh print nhi karta sirf result deta hai, Tum uss result se aagey kaam kartey ho

# bina return k 

# def kashish(a,b):
#     print(a+b)

# def kashish(a,b):
#     # xyz
#     return(a+b)


# result = kashish(4,5)


# print(f" result {result}")

# return k baad function band ho jata hai chahey aur code ho neeche woh nhi chalega

# def check(number):
#     if number>0:
#         return "positive"
#     return "Negative"

# result = check(8)

# print(result)

# return se value flexible ho jaati hai and
# print se value screen par show hoti hai 

# bina return k - limited use

# def calculate_tax(income):
#     print(income*0.1)

# calculate_tax(9000)

# return k saath


# def calculate_tax(income):
#     return income*0.1

# tax=calculate_tax(9000)


# # calculation mai uss value ko use karenge

# net_income = 50000-calculate_tax(50000)

# # condition main use kar skatey hain

# if calculate_tax(50000)>4000:
#     print("high tax")




# print(f"tax:{calculate_tax(50000)}")


# multiple values bhi return kar saktey hain

def student_result(marks):
    percentage = (marks/100)*100

    if marks>=90:
        grade ="A"
    elif marks >= 80:
        grade ="B"

    else:
        grade="c"

    return percentage, grade


per, grad=student_result(85)

print(f"Percentage:{per}")
print(f"grade:{grad}")
age=15
income=50000
has_property=True


# AND - sab conditions true hona chahiye
if age>=18 and income>30000 and has_property:
    print("You are eligible for the loan.")
# OR - ek condition true hona chahiye
if age>=18 or income>30000 or has_property:
    print("You might be eligible for the loan.")

# NOT - condition ko invert karta hai
is_blocked=False
if not is_blocked:
    print("You can access the account.")

# combination of logical operators
if (age>=18 and income>30000) or has_property:
    print("You are eligible for the loan.")
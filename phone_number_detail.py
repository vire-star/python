import phonenumbers

from phonenumbers import timezone,geocoder, carrier

# Take phone number from user
number=input("enter your number")

# Make a variable 
phone=phonenumbers.parse(number)

# Time zone
time=timezone.time_zones_for_number(phone)

car=carrier.name_for_number(phone,"en")

# Registration
reg=geocoder.description_for_number(phone,"en")

print( time)
print(phone)
print(car)
print(reg)
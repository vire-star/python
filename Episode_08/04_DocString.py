# DocString
# 

def calculate_bmi(weight,height):
    """
    BMI calculate karta hai
     
    parameter:
    weight(float)
    height(float)

    example:
    >>> calculate_bmi(70,1.75)
    """
    bmi  = weight/(height**2)
    return round(bmi,2)
def is_rational(number):
    try:
        float_number = float(number)
        numerator, denominator = float_number.as_integer_ratio()
        return True
    except:
        return False

number = input("Enter a number: ")

if is_rational(number):
    print(f"{number} is a rational number.")
else:
    print(f"{number} is not a rational number.")

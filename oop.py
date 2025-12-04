def check_number(num):
    if num > 0:
        return "The number is Positive"
    elif num < 0:
        return "The number is Negative"
    else:
        return "The number is Zero"

print(check_number(10))
print(check_number(-5))
print(check_number(0))
def sum_of_digits(number):
    str_number = str(number)
    
    digit_sum = 0
    
    for digit in str_number:
        digit_sum += int(digit) 
    
    return digit_sum

number = int(input("Enter a number: "))

result = sum_of_digits(number)
print(f"The sum of digits of {number} is: {result}")

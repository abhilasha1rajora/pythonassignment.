# Function to check if a number is even or odd
def check_even_odd(number):
    if number % 2 == 0:
        return f"{number} is even."
    else:
        return f"{number} is odd."

# Take input from the user
try:
    num = int(input("Enter a number: "))
    # Call the function and print the result
    result = check_even_odd(num)
    print(result)
except ValueError:
    print("Please enter a valid integer.")


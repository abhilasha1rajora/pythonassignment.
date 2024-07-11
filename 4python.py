# Taking input from the user
user_input = input("Enter a string: ")

# Opening a text file in write mode
file_name = "user_input.txt"
with open(file_name, 'w') as file:
    # Writing the user input to the file
    file.write(user_input)

print(f"Successfully wrote '{user_input}' to '{file_name}'")

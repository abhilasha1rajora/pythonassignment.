# Specify the file name to read from
file_name = "sample.txt"

try:
    # Open the file in read mode
    with open(file_name, 'r') as file:
        # Read each line and print it
        for line in file:
            print(line, end='')  # 'end='' to avoid double spacing between lines
        
except FileNotFoundError:
    print(f"Error: The file '{file_name}' was not found.")
except IOError:
    print(f"Error: Could not read from the file '{file_name}'.")

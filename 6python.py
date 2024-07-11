
file_name = "hello.txt"

try:
    
    with open(file_name, 'r') as file:
        
        file_content = file.read()
        
        
        print("Content of the file:")
        print(file_content)
        
except FileNotFoundError:
    print(f"Error: The file '{file_name}' was not found.")
except IOError:
    print(f"Error: Could not read from the file '{file_name}'.")

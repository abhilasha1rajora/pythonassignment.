def check_substring(main_string, substring):
    if substring in main_string:
        return True
    else:
        return False

main_string = input("Enter the main string: ")
substring = input("Enter the substring to check: ")

if check_substring(main_string, substring):
    print(f"'{substring}' is present in '{main_string}'.")
else:
    print(f"'{substring}' is not present in '{main_string}'.")

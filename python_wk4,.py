filename = input("Enter the name of the file you want to read: ")

try:
    with open(filename, "r") as file:
        content = file.read()
        print(f"\nSuccessfully read the content of '{filename}':")
        print(content)
except FileNotFoundError:
    print(f"\nError: The file '{filename}' was not found.")
except PermissionError:
    print(f"\nError: You don't have permission to read the file '{filename}'.")
except Exception as e:
    print(f"\nAn unexpected error occurred while reading '{filename}': {e}")
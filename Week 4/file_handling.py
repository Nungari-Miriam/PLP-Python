data = input("Enter file path: ")

try:
    # Open the file for READING
    with open(data, "r") as file: 
        content = file.read()
        print(content)

    # Modify the content 
    modified_content = content.upper()
    
    # Write modified content to a new file
    new_file = "modified_output.txt"
    with open(new_file, "w") as f:
        f.write(modified_content)
        print(modified_content)

    print(f"Modified content has been written to '{new_file}'.")

# Error Handling
except FileNotFoundError:
    print("Error: File not found. Please check the path.")
except PermissionError:
    print("Error: You don’t have permission to read this file.")
except Exception as e:
    print(f"Unexpected error: {e}")

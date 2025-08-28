# file_read_write.py

def modify_file(input_file, output_file):
    try:
        # Open the input file in read mode
        with open(input_file, "r") as infile:
            content = infile.read()

        # Example modification: convert to uppercase
        modified_content = content.upper()

        # Write the modified content into the new file
        with open(output_file, "w") as outfile:
            outfile.write(modified_content)

        print(f"✅ Successfully created '{output_file}' with modified content.")

    except FileNotFoundError:
        print(f"❌ Error: The file '{input_file}' was not found.")
    except PermissionError:
        print(f"❌ Error: Permission denied when accessing '{input_file}'.")
    except Exception as e:
        print(f"⚠️ An unexpected error occurred: {e}")


# Example usage
if __name__ == "__main__":
    modify_file("input.txt", "output.txt")

# error_handling_lab.py

def read_user_file():
    filename = input("📂 Enter the filename to read: ")

    try:
        with open(filename, "r") as f:
            content = f.read()
            print("\n📖 File Content:")
            print(content)

    except FileNotFoundError:
        print(f"❌ Error: The file '{filename}' does not exist.")
    except PermissionError:
        print(f"❌ Error: You do not have permission to read '{filename}'.")
    except Exception as e:
        print(f"⚠️ Unexpected error: {e}")


# Run the program
if __name__ == "__main__":
    read_user_file()

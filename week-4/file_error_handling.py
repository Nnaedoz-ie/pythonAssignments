def get_filename_and_read():
    filename = 'sample.txt'  # Default file name for testing

    try:
        # Try to open the file and read it
        with open(filename, 'r') as file:
            content = file.read()
            print("File content:")
            print(content)

    except FileNotFoundError:
        print(f"Error: The file {filename} does not exist.")
    except IOError:
        print(f"Error: There was an issue reading the file {filename}.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Example usage
get_filename_and_read()

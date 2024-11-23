def read_and_modify_file():
    input_filename = 'input.txt'  # The file you want to read from
    output_filename = 'output.txt'  # The file to save the modified content

    try:
        # Open the input file in read mode
        with open(input_filename, 'r') as infile:
            content = infile.read()

        # Modify the content (e.g., converting to uppercase)
        modified_content = content.upper()

        # Open the output file in write mode and save the modified content
        with open(output_filename, 'w') as outfile:
            outfile.write(modified_content)
        
        print(f"File successfully written to {output_filename}")
    
    except FileNotFoundError:
        print(f"Error: The file {input_filename} was not found.")
    except IOError:
        print("Error: There was an issue with reading or writing the file.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Call the function to execute
read_and_modify_file()

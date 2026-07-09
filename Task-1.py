try:
    # Open the file in read mode
    file = open("sample.txt", "r")

    print("Reading file content:\n")

    line_number = 1

    # Read file line by line
    for line in file:
        print("Line", line_number, ":", line.strip())
        line_number += 1

    # Close the file
    file.close()

except FileNotFoundError:
    print("Error: The file 'sample.txt' was not found.")

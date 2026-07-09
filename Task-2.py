# Take input from user
text = input("Enter text to write to the file: ")

# Write data to file
file = open("output.txt", "w")
file.write(text + "\n")
file.close()

print("Data successfully written to output.txt.")

# Take additional input
append_text = input("Enter additional text to append: ")

# Append data
file = open("output.txt", "a")
file.write(append_text + "\n")
file.close()

print("Data successfully appended.")

# Read final content
print("\nFinal content of output.txt:")

file = open("output.txt", "r")

for line in file:
    print(line.strip())

file.close()

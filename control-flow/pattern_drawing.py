# pattern_drawing.py

# Prompt the user for the pattern size
size = int(input("Enter the size of the pattern: "))

# Initialize row counter
row = 0

# Use while loop for rows
while row < size:
    # Use for loop for columns (printing asterisks)
    for col in range(size):
        print("*", end="")
    print()  # Move to next line after printing one row
    row += 1

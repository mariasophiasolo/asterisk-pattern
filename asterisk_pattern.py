# creating an asterisk pattern

# Set the number of rows for the pyramid
num_rows = 5

# Loop to print the downward half-pyramid pattern
for i in range(num_rows, 0, -1):
    for j in range(i):
        print("*", end=" ")
    
    # Move to the next line after each row
    print()

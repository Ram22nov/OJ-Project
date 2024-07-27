# Get input from the user
number = int(input())

# Initialize the factorial result
factorial = 1

# Calculate the factorial
for i in range(1, number + 1):
    factorial *= i

# Print the factorial
print(factorial)
# Get input from the user
number = int(input())

# Initialize the sum of digits
sum_of_digits = 0

# Handle negative numbers by taking the absolute value
number = abs(number)

# Calculate the sum of digits
while number > 0:
    sum_of_digits += number % 10
    number //= 10

# Print the sum of digits
print(sum_of_digits)
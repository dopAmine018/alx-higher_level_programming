import random

# Generate a random signed number
number = random.randint(-10, 10)

# Print the generated number
print(number, end=' ')

# Check if the number is positive, negative, or zero, and print the corresponding message
if number > 0:
    print("is positive")
elif number < 0:
    print("is negative")
else:
    print("is zero")

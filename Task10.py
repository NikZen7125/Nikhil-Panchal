# Task 10 - Palindrome Number

# Prompt the user to input a number
num = int(input("Enter a number:"))

# Function to reverse the digits of the given number
def reverseNum(num):
    rev = 0  # Initialize a variable to store the reversed number
    
    # While loop to reverse the number by extracting digits from the right
    while num > 0:
        rem = num % 10  # Get the last digit of the number
        rev = rev * 10 + rem  # Build the reversed number
        num = num // 10  # Remove the last digit from the original number

    return rev  # Return the reversed number

# Check if the reversed number is the same as the original number
if reverseNum(num) == num:
    print("Number is Palindrome")
else:
    print("Number is not Palindrome")

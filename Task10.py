# Task 10 - Palindrome Number

num = int(input("Enter a number:"))

# Function to reverse the digits of the given number
def reverseNum(num):
    rev = 0 # Variable to store reversed number
    
    # Loop to reverse the number
    while num > 0:
        rem = num % 10  # Get the last digit of the number
        rev = rev * 10 + rem  # Build the reverse number
        num = num // 10  # Remove the last digit from the number
    return rev

# Check if the reversed number is the same as the given number
if reverseNum(num) == num:
    print("Number is Palindrome")
else:
    print("Number is not Palindrome")

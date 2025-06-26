# Task 12 - Cows and Bulls Game

import random

print("Welcome to Cows and Bulls Game!")

# Generate a random 4-digit number between 1000 and 9999
random_num = str(random.randint(1000, 9999))

# random_num = "2966"

# Function to calculate the number of cows and bulls
def gen_cows_bulls(num):
    cows = 0  # Initialize cows counter (correct digits in correct position)
    bulls = 0  # Initialize bulls counter (correct digits in incorrect position)
    bullNum = []  # List to hold digits from the user's guess that are not in the correct position
    bullRandom = []  # List to hold digits from the random number that are not in the correct position
    
    # Loop over the 4 digits of the guess and the random number
    for i in range(4):
        if num[i] == random_num[i]:
            cows += 1  # If digit in the same position, it's a cow (correct guess)
        else:
            bullNum.append(num[i])  # If not correct position, add to bullNum (user guess)
            bullRandom.append(random_num[i])  # Add to bullRandom (actual number)
    
    # Count the bulls (correct digits in wrong positions)
    for j in bullNum:
        if j in bullRandom:  # If a digit from the guess exists in the random number
            bullRandom.remove(j)  # Remove it from the random number list to avoid double counting
            bulls += 1  # Increment bulls count
    
    # Return the final counts of cows and bulls
    return cows, bulls

# Start the game loop
while True:
    # Prompt the user to input a guess
    guess = input("\nGuess the number: ")
    
    # Call the gen_cows_bulls function to calculate cows and bulls
    cows, bulls = gen_cows_bulls(guess)
    
    # Print the result of the guess
    print(f"{cows} cows, {bulls} bulls")
    
    # If the user guesses all 4 digits correctly (4 cows), end the game
    if cows == 4:
        print("Correct Guess!")
        break  # Exit the loop

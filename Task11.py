# Task 12 - Cows and Bulls Game

import random

print("Welcome to Cows and Bulls Game!")

# Generate a random 4-digit number
random_num = str(random.randint(1000, 9999))

# Function to calculate cows and bulls
def gen_cows_bulls(num):
    cows, bulls = 0, 0
    bullNum, bullRandom = [], []
    
    # Check for cows and prepare lists to check bulls
    for i in range(4):
        if num[i] == random_num[i]:
            cows += 1
        else:
            bullNum.append(num[i])
            bullRandom.append(random_num[i])
    
    # Count bulls
    for j in bullNum:
        if j in bullRandom:
            bullRandom.remove(j)
            bulls += 1
    
    return cows, bulls

# Game loop
while True:
    guess = input("\nGuess the number: ")
    
    cows, bulls = gen_cows_bulls(guess)
    
    print(f"{cows} cows, {bulls} bulls")
    
    if cows == 4:
        print("Correct Guess!")
        break

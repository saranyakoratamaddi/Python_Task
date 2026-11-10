#Create a Number Guessing Game where: 
#● The program generates a random number between 1 and 50 using random. 
#● The user has 5 attempts to guess the number. 
#● After each guess, calculate the absolute difference using math.fabs() and display how far the guess is from the correct number.




import random
import math
num=random.randint(1,50)
print("Guess The Number between 1 to 50")
print("You have 5 Attempts to guess the Number")
for attempt in range(1,6):
    guess=int(input(f"Attempt {attempt}/5 Enter your guess:"))
    diff=math.fabs(guess-num)
    print(f"Your Guess is incorrect. you are {diff} away from the number")

    if guess==num:
            print("Congratulations! You Guessed the Correct number")
            break
            diff=math.fabs(guess-num)
            print(f"Your Guess is incorrect. you are {diff} away from the number")
print("Game Over The correct number was:",num)

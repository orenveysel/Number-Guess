'''
    A number that will be generated randomly between 1-100 and 4, with roughly
    try to find it.
    ** Search "python random" for "random module."
    ** Rating through 100. Every question is 20 points.
    ** Get the Rights from the user and each question is the specified number of lives
    calculate over.
'''

import random

x = random.randint(1,100)

print("***** WELCOME TO THE NUMBER GUESSING GAME *****")

live = int(input("How many lives do you want to start with?: "))
point = 100/live

i = 0
score = 100
while i < live:
    a = int(input("Take a guess: "))
    
    if i + 1 == live:
        print("Your lives are over!")
        print(f"The number was {x}:( ")
        print("Your score is 0")
        break
    if a == x:
        print(f"Congratulations, you found the number in the {i+1}. attempt!")
        print(f"Your score is {score:1.4}")
        break
    elif a < x:
        print("Up!!")
    elif a > x:
        print("Down!!")   
    i += 1
    score -= point
    

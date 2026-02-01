# Number guessing game
import random

# explaination to user
prompt = "###\nThis is a guessing number game, so create a range and guess what number selected by computer!\nGood Luck\n"
print(prompt)

# starting number (lower)
l = int(input("Enter a number for starting range: "))

# ending number (greater)
g = int(input("Enter a number for ending range: "))

print(f"\nYou have 7 chances to guess computer number between {l} and {g} .Let's start!")
# computer number
c = random.randint(l, g)
# changces & guess counter
ch = 7
gc = 0

# main loop
while ch >= gc:
    if ch == gc:
        print(f"The computer number was {c}")
        print("Better luck next time!")
        break
    # user guessing
    u = int(input(f"Guess {gc+1}: "))
    if c == u:
        print(f"Congratulations! The number is {c}")
        print(f"Total Guessings: {gc+1}")
        break
    elif c > u:
        print("Try Again! You guessed too small!")
    else:
        print("Try Again! You gessed too high!")
    gc += 1
print("###")

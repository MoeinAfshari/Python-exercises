# Word Guessing Game
import random

# get name & show it to user
name = input("\nWhat is your name? ")
prompt = f"Good Luck! {name}\nGuess the characters\n"
print(prompt)

# these words and a word select randomly
words = ["python", "geeks", "reserve", "devops", "developer", "programming", "program"]
word = random.choice(words)

# in the first, user guesses are empty, has 12 turns, the first turn is zero trun and f is a flag that shows word is in guesses completely or not
guesses = ''
turns = 12
turn = 0
f = False

# this loop shows to user number of characters in the first, checks sorted word & guesses are equal and gets character from user
while turns > turn:
    for i in word:
        if i in guesses:
            print(i)
        else:
            print('_')
        print()
    if sorted(word) == sorted(guesses):
        f = True
        print("You Win!")
        print(f"The word is {word}")
        break
    g = input("Guess a character: ")
    if g in word:
        c = word.count(g)
        for i in range(c):
            guesses += g
    turn += 1

# if the turns finished and the user didn't guess, gets a message 
if turn == 12 and f == False:
    print("You Loose!")

################################
# geeksforgeeks solution
#import random
#name = input("What is your name? ")
#print("Good Luck ! ", name)
#words = ['rainbow', 'computer', 'python', 'science', 'programming', 'geeks']
#word = random.choice(words)
#print("Guess the characters")
#guesses = ''
#turns = 12
#while turns > 0:
#    failed = 0
#    for char in word:
#        if char in guesses:
#            print(char, end=" ")
#        else:
#            print("_")
#            failed += 1
#    if failed == 0:
#        print("You Win")
#        print("The word is: ", word)
#        break
#    print()
#    guess = input("guess a character: ")
#    guesses += guess
#    if guess not in word:
#        turns -= 1
#        print("Wrong")
#        print("You have ", + turns, 'more guesses')
#        if turns == 0:
#            print("You Loose")

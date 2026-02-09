# Hangman game python
import random

# get words as multi lines & convert them to an array
words = '''apple banana mango strawberry orange grape pineapple apricot lemon coconut watermelon cherry papaya berry peach lychee muskmelon'''
words = words.split(' ')

# program works when runs directly
if __name__ == "__main__":
    prompt = "Guess the word! HINT: word is a name of a fruit"
    print(prompt)
    word = random.choice(words)
    guesses = ''
    turns = len(word) + 2

    while turns >= 0:
        failed = 0
        for char in word:
            if char in guesses:
                print(char, end=' ')
            else:
                print('_', end=' ')
                failed += 1
        print()
        if failed == 0:
            print("Congratulations, you won!")
            break
        turns -= 1
        if turns == -1:
            print("You Loose!")
            print(f"The word was {word}")
            break
        g = input("Enter a letter to guess: ")
        guesses += g
else:
    print("Please run program directly!")

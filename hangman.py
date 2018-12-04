import random

with open('sowpods.txt', 'r') as f:
    words_base = f.read().split('\n')

def pick_a_word():
    return random.choice(words_base)

def guessing():
    printek = '\n'
    for i in field:
        printek += i + ' '
    print(printek)
    letter = input("\nGuess the letter: ")
    if letter.lower() in word or letter.upper() in word:
        for i in [pos for pos, char in enumerate(word) if char == letter.upper()]:
            field[i] = letter.upper()
    else:
        print("\nWrong! Try again.")

x = pick_a_word()
word = list(x)
field = list(len(word)*'_')
print("Welcome in the Hangman game! Discover the word, by guessing letter by letter.")
print(word)
while word != field:
    guessing()
print("Congrats, You won! The missed word was:", x)

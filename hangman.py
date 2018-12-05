import random

with open('sowpods.txt', 'r') as file:
    words_base = file.read().split('\n')

counter = 6

def pick_a_word():
    return random.choice(words_base)

def guessing():
    printek = '\n'
    for i in field:
        printek += i + ' '
    print("\nYou have", counter, "chances left.")
    print(printek)
    letter = input("\nGuess the letter: ")
    if letter.lower() in word or letter.upper() in word:
        for i in [pos for pos, char in enumerate(word) if char == letter.upper()]:
            field[i] = letter.upper()
        return 0
    else:
        if counter > 1:
            print("\nWrong! Try again.")
        else:
            print("\nWrong!")

        return 1

x = pick_a_word()
word = list(x)
field = list(len(word)*'_')

print("Welcome in the Hangman game! Discover the word, by guessing letter by letter.")
print(x)
while word != field and counter > 0:
    counter -= guessing()
if word == field:
    print("Congrats, You won! The missed word was:", x)
else:
    print("\nSorry, You lose. The missed word was:", x)

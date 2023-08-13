import random


def print_scaffold(guesses):  # prints the scaffold
    if guesses == 0:
        print("_________")
        print("|	 |")
        print("|")
        print("|")
        print("|")
        print("|")
        print("|________")
    elif guesses == 1:
        print("_________")
        print("|	 |")
        print("|	 O")
        print("|")
        print("|")
        print("|")
        print("|________")
    elif guesses == 2:
        print("_________")
        print("|	 |")
        print("|	 O")
        print("|	 |")
        print("|	 |")
        print("|")
        print("|________")
    elif guesses == 3:
        print("_________")
        print("|	 |")
        print("|	 O")
        print("|	\|")
        print("|	 |")
        print("|")
        print("|________")
    elif guesses == 4:
        print("_________")
        print("|	 |")
        print("|	 O")
        print("|	\|/")
        print("|	 |")
        print("|")
        print("|________")
    elif guesses == 5:
        print("_________")
        print("|	 |")
        print("|	 O")
        print("|	\|/")
        print("|	 |")
        print("|	/ ")
        print("|________")
    elif guesses == 6:
        print("_________")
        print("|	 |")
        print("|	 O")
        print("|	\|/")
        print("|	 |")
        print("|	/ \ ")
        print("|________")
        print("\n")


WORDS = ["python", "work", "time", "girl", "game", "month"]
word = random.choice(WORDS)


length = len(word)

b = list(length * "-")
print(*b)
attempts = 6
guesses = 0

while attempts > 0:
    letter = input("please Enter Letter = ")

    if letter in word:
        for i in range(length):
            if letter == word[i]:
                b[i] = letter
                print(*b)
                if "-" not in b:
                    print("win")
                    break

    else:
        guesses += 1
        print_scaffold(guesses)

        print("try Agin")
        attempts -= 1
else:
    print(" lose")

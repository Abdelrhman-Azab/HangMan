import random
import os

fruits = ["mango", "banana", "apple", "watermelon", "pineapple", "strawberry", "blueberry"]
ran = random.randint(0, len(fruits) - 1)
charNumber = len(fruits[ran])
arr = []
for i in range(charNumber):
    arr.append(' - ')
clear = lambda: os.system('cls')
x = ''
Win = False
right = 0
wrong = 0
fail = 0
Failed = False
Number_of_Try = 3


def draw():
    print("\t\t\tWelcome to Hangman\t")
    print(f"\t\t\tYou have {Number_of_Try} chances")
    print("\t\t\tGuess the fruit to save the guy")
    print("")
    if Number_of_Try < 3:
        print("\t\t\t\t|")
        print("\t\t\t\t|")
        print("\t\t\t\tO")
    if Number_of_Try < 2:
        print("\t\t\t       \|/")
    if Number_of_Try < 1:
        print("\t\t\t        | ")
        print("\t\t\t       /|\ ")

    print("\n\n\n")
    print("\t\t\t\t\t\t", end='')
    for i in arr:
        print(i, end='')
    print()


while not Win and not Failed:
    draw()
    print()
    x = input("\t\t\tGuess the fruit alphabetic : ")
    for i in range(len(fruits[ran])):
        if x == fruits[ran][i]:
            arr[i] = f"{x}"
            right += 1
    if right == wrong:
        fail += 1
        Number_of_Try -= 1
    right = wrong
    if fail == 3:
        Failed = True
    clear()
    if ' - ' not in arr:
        Win = True

if Win:
    clear()
    print("We have Winner")
if Failed:
    draw()
    print("Wrong answer ,Good luck next time ! ")

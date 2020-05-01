import random

libary = ['house','car','dog','cat','street']
word = random.choice(libary)

if word == 'house':
    print("the thing i am thinking of can be found along a street")
if word == 'car':
    print("it can go brum brum and beep beep")
if word =='dog':
    print("it can go woof woof")
if word == 'cat':
    print("it is furry and says meowww!!")
if word == 'street':
    print("you walk on it?")

while True:
    guess = input("guess what the word is?")
    if guess == word:
        print("thats the right answer")
    else:
        print("that is wrong")
        break



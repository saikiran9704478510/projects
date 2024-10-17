from random import randint

n = randint(1,100)
a = -1
guesses = 1

while (a!=n):
    a = int(input("guess a number between 1 and 100: "))
    if(a > n):
        print("lower number pls")
        guesses += 1
    elif(a < n):
        print("higher number pls")
        guesses += 1

print(f"you have guessed the number {n} in {guesses} attempts")

## THE PERFECT GUESS:

import random
n= random.randint(1, 101)
print("The Game is starting...")
print("RULES: Guess a number between 1 and 100❗")

a=-1
guesses = 0
try:
    while(a != n):
        a=int(input("Guess the number: "))
        if (a >= 100 or a<= (-1)):
            print("Invalid input given. Try again!")
        elif (a < n):
            print("Higher number please ⬆️")
        elif (a > n):
            print("Lower number please ⬇️")
        guesses+=1
    print(f"🎉 You have guessed the number \"{n}\" correctly in {guesses} attempts")

except ValueError:
    print('Are you blind? I said "NUMBER"😑!!')
except Exception as e:
    print(e)


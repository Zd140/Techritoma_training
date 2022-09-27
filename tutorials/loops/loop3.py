import random

n = random.randint(1, 100)

print(n)
guess = int(input('Enter a interger between 1 to 100: '))

while n != "guess":
    if guess < n:
        print("Your guesss is low")
        guess = int(input('Enter an interger between 1 to 100:'))
    elif guess > n:
        print('Your guess is high')
        guess = int(input('Enter an inter between 1 to 100: '))
    else:
        print('You guest it correctly')
        break
    print()
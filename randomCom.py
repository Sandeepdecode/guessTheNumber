import random

def guess(x):
    random_number = random.randint(1,x)
    guess = 0
    guess_no = 0
    while True:
        try:
            guess = int(input(f'Guess a number between 1 and {x}: '))
        except ValueError:
            print("Please, enter a valid number !!")
            continue
        guess_no += 1
        if guess == random_number:
            print(f'Yay, congrats. YOU HAVE GUESS THE NUMBER {random_number} correctly !!! ')
            print(f'You guessed the number in {guess_no - 1} tries')
            break
        elif guess < random_number:
            print('Sorry,  guess again. Too low')
        elif guess > random_number:
            print('Sorry,  guess again. Too High')

x = int(input("Input the range of guess: "))
guess(x)
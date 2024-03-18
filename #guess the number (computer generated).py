#guess the program generated number project

import random

def guess(x):
    random_number = random.randint(1,x)
    guess = 0
    while guess != random_number:
        guess = int (input(f'Guess a number between 1 and {x}: '))
        if guess < random_number: 
            print ('Your guess is too low.')
        elif guess > random_number > random_number:
            print('Your guess is too high.')
    
    print(f'Your guess is correct! {random_number} is the right answer.')

def computer_guess(x):
    low = 1
    high = x
    feedback = ''
    while feedback != 'Correct':
        guess = random.randint(low, high)
        feedback = input(f'Is {guess} too high or too low ?')
        if feedback == 'high':
            high = guess - 1
        elif feedback == 'low':
            low = guess + 1

    print (f'The program guess your number, {guess} correctly!')

guess(10)
 
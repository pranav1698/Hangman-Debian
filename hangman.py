import time
import random

# Welcome
name = input('What is your name? \n')

print("Hello, " + name + " Ready for hangman!")

print(' ')

# Wait for 1 second
time.sleep(1)

print("Start Guessing!")
time.sleep(0.5)

turns = 10

words = ['chicago', 'canberra', 'mumbai', 'sydney', 'paris']
random = random.randrange(0, 4, 1)
word = words[random]

guesses = ''
failed = 0

while turns > 0:
	guess = input('Make a guess?')
	if guess in word:
		for char in word:
			if guess == char or char in guesses:
				print(char, end=' ')
				guesses += char
			else:
				print('_', end=' ')
		print('\n')
		if set(word) == set(guesses):
			print('You won!!!')
			break
	else:
		turns -= 1
		print("Wrong! You have, "+ str(turns) + " more guesses")
		failed += 1
		

if failed >= 3:
	print('You lose')
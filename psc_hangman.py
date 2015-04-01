import random

def hangman():

	
	username = raw_input ("First and Last Name:") #User enters his/her name
	#Create word lists depending on user
	if username == 'Alex Lindo':
		hangman_list = ['koalassucker']
	else:
		hangman_list = ["van", "two", "example", "says", "python", "rocks", "vanilla"]
	#While loop runs through entire game
	again = True
	while again: 
	
		play_word = random.choice(hangman_list) #Randomly select a word
		blanks = "_"*len(play_word) #Store blanks in variable
		correctLetters = set() #Empty set list for correct letters
		strikeLetters = set() #Empty set list for strikes
		strikes = 7 #Set the strikes allotted to 7 chances:
		print "Your word has %d letters:" %(len(play_word))
		print (" ".join(blanks))
	
		guessed = False
		while not guessed and strikes>0:
			guess_letter = raw_input ("Guess a letter: ").rstrip() #Prompt for letter
			valid_letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
			if guess_letter not in valid_letters:
				print "This is not a valid letter."
				guess_letter = raw_input ("Guess a letter: ").rstrip()
			if guess_letter in correctLetters:
				print "You already used this letter!"
			if guess_letter in strikeLetters:
				print "You already used this letter!"
				guess_letter = raw_input ("Guess a letter: ").rstrip()
			if guess_letter in play_word:
				correctLetters.add(guess_letter)
				blanks = "".join([char if char in correctLetters else "_" for char in play_word])
				print "Good guess!"
				if blanks == play_word:
					guessed = True
					print "You won!"
					y=True
					n=False
					again = (input("Would you like to go again? [y/n]: "))
					if again == y:
						return hangman()
					else:
						quit()
			else:
				strikes -= 1 #It subtracts 1 from the 7 allotted mistakes
				strikeLetters.add(guess_letter)
				print "Wrong letter! You have %d strikes left. Wrong letters used: " %(strikes) + ("".join(strikeLetters))
				if strikes == 0: 
					print "You lost! The word was: " + play_word
					y=True
					n=False
					again = (input("Would you like to go again? [y/n]: "))
					if again == y:
						return hangman()
					else:
						quit()
			print (" ".join(blanks))
						

###Draw the hangman:
##Draw the pole
##Draw underscores for each letter in the chosen word
##Draw body parts for each strike (6 strikes max.)

if __name__=="__main__":
	hangman()
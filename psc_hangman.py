import random

def playHangman():

	hangmanPics = ['''

	       +---+
	       |   |
	           |
	           |
	           |
	           |
	     =========''', '''
	    
	       +---+
	       |   |
	       O   |
	           |
	           |
	           |
	     =========''', '''
	    
	       +---+
	       |   |
	       O   |
	       |   |
	           |
	           |
	     =========''', '''
	    
	       +---+
	       |   |
	       O   |
	      /|   |
	           |
	           |
	     =========''', '''
	    
	       +---+
	       |   |
	       O   |
	      /|\  |
	           |
	           |
	     =========''', '''
	    
	       +---+
	       |   |
	       O   |
	      /|\  |
	      /    |
	           |
	     =========''', '''
	    
	       +---+
	       |   |
	       O   |
	      /|\  |
	      / \  |
	           |
	     =========''']
	
	username = raw_input ("First and Last Name: ") #User enters his/her name
	if username == 'Alex Lindo': #Create word lists depending on user
		hangman_list = ["koala_sucker"]
	else:
		hangman_list = ["python", "blue", "vanilla"]
	
	again = True
	while again: #While loop runs through entire game
	
		play_word = random.choice(hangman_list) #Randomly select a word
		blanks = "_"*len(play_word) #Store blanks in variable
		correctLetters = set() #Empty set list for correct letters
		strikeLetters = set() #Empty set list for strikes
		strikes = 6 #Set the strikes allotted to 6 chances:
		pic = 0 #Sets the index of hangmanPic to 0

		if username == 'Alex Lindo':
			print "There are two words with 5 and 6 letters."
			print "_ _ _ _ _  _ _ _ _ _ _"
		else:
			print "Your word has %d letters:" %(len(play_word))
			print (" ".join(blanks))
	
		guessed = False
		while not guessed and strikes>0: #While loop runs through unguessed word
			guess_letter = raw_input ("Guess a letter: ").rstrip() #Prompt for letter, check if valid
			valid_letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
			if guess_letter not in valid_letters:
				print "This is not a valid letter."
				guess_letter = raw_input ("Guess a letter: ").rstrip()
			if guess_letter in correctLetters:
				print "You already used this letter!"
			if guess_letter in strikeLetters:
				print "You already used this letter!"
				guess_letter = raw_input ("Guess a letter: ").rstrip()
			if guess_letter in play_word: #Adds correct letters to set list, prints
				correctLetters.add(guess_letter)
				blanks = "".join([char if char in correctLetters else "_" for char in play_word])
				print "Good guess!"
				if blanks == play_word: #If list of guessed letters correct, win
					guessed = True
					print "You won!"
					y=True 
					n=False
					again = (input("Would you like to go again? [y/n]: ")) #Prompts play again
					if again == y:
						return playHangman()
					else:
						quit()
			else:
				strikes -= 1 #Subtracts 1 from the 6 allotted mistakes
				strikeLetters.add(guess_letter) #Adds wrong letters to set list, prints
				pic += 1 #Sets the index
				print "Wrong letter! You have %d strikes left. Wrong letters used: " %(strikes) + ("".join(strikeLetters))
				print (hangmanPics[pic]) #Prints the hangman at each strike
				if strikes == 0: #If all strikes used, lost
					print "You lost! The word was: " + play_word
					y=True
					n=False
					again = (input("Would you like to go again? [y/n]: "))
					if again == y:
						return playHangman()
					else:
						quit()
			print (" ".join(blanks)) #Prints blanks with guessed letters
						


if __name__=="__main__":
	playHangman()
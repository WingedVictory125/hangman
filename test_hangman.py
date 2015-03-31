import random

def Playing():
	listOfWords = ["example", "says", "python", "rocks"]
	
	again = True
	while again:

		guessWord = random.choice(listOfWords)
		board = "_" * len(guessWord)
		correctGuess = set() #Creates an unordered collection of elements with no duplicates
		strikes = 7 #The strikes start at 7
		#strikesboard = ["*" for char in guessWord]

		print(" ".join(board)) #joins other letters or replaces the guessed letters

		guessed = False
		while not guessed and strikes>0:
			guess = raw_input("Guess a letter: ").rstrip()
			if guess in guessWord:
				correctGuess.add(guess) #Creates a list of the guessed letters
				board = "".join([char if char in correctGuess else "_" for char in guessWord])
				if board == guessWord:
					guessed = True
					print "You won!"		
			else:
				strikes -= 1 #It subtracts 1 form the 7 alloted mistakes
				print "Wrong letter! You have %d strikes left." %(strikes) #Tells you how many strikes are left
			
				if strikes == 0:
						print "You lost! The word was: " + guessWord
					
			print(" ".join(board))
			
		y = True
		n = False
		again = (input("Would you like to go again? [y/n]: ") == 'y')
		Playing()
		###Add n --> quit()
			
Playing() #Displays playing without you having to type it

if guess_letter not in play_word:
				strikeLetters.add(guess_letter)
				strike_list= "".join([char if char in strikeLetters else "_" for char in play_word])
				print(" ".join(strike_list))
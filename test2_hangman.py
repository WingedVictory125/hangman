import random

strikeLetters = set()
strikes = 7

def hangman():
#Ask user to enter his/her name
	username = raw_input ("First and Last Name:")
#Create word lists depending on user
	if username == 'Alex Lindo':
		hangman_list = ['koala sucker']
	else:
		hangman_list = ['van', 'two']
#Randomly select a word
	word = random.choice(hangman_list)
#Split the word into letters
	play_word = list(word)
	print play_word
#Store blanks in variable and print
	blanks = "_"*len(play_word)
	print "Your word has %d letters:" %(len(play_word)) + blanks
#Create an empty set list for strikes:
	strikeLetters = set()
#Set the strikes allotted to 7 chances:
	
#Prompt user to guess a letter
	ask4letter(play_word, blanks)
#--Check if raw input is valid, else prompt user to give a new letter
def ask4letter(play_word, blanks):
	guess_letter = raw_input ("Guess a letter from a to z: ").rstrip()
	valid_letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
	while guess_letter not in valid_letters:
		print "This is not a valid letter."
		guess_letter = raw_input ("Guess a letter from a to z: ").rstrip()
	check_letter(guess_letter, play_word, blanks)
#Check if guessed letter is in the play word
#--If guessed letter is in the word --> return blanks w/replaced letters
#--If guessed letter not in word --> check strikes
def check_letter(guess_letter, play_word, blanks):	
	for i in range(len(play_word)):
		if guess_letter == play_word[i]:
			blanks = list(blanks)
			blanks[i] = guess_letter
			###Needs fix, not adding double letters to blanks
			print "Good guess!"
			print blanks
			if blanks == play_word:
				print "You won!"
				y=True
				n=False
				again = (input("Would you like to go again? [y/n]: "))
				if again == y:
					return hangman()
				else:
					quit()
			else:
				ask4letter(play_word, blanks)
		else:
			check_strikes(play_word, guess_letter, blanks)

#If guessed letter is not in word, create list of wrong letters
def check_strikes(play_word, guess_letter, blanks):
	#####---Should I add a list of cummulative wrong letters?
	print "The strikes are %d" %strikes
	while guess_letter not in play_word and strikes>0:
		strikes -= 1 #It subtracts 1 form the 7 allotted mistakes
		####Needs fix, not subtracting
		print "Wrong letter! You have %d strikes left." %(strikes) 
		ask4letter(play_word, blanks)
	if strikes == 0:
		print "You lost! The word was: "
		print play_word
		y=True
		n=False
		again = (input("Would you like to go again? [y/n]: "))
		if again == y:
			return hangman()
		else:
			quit()

#####--What happens if user repeats a letter that was already 
#####--added to guessed blanks/strikes?

###Draw the hangman:
##Draw the pole
##Draw underscores for each letter in the chosen word
##Draw body parts for each strike (6 strikes max.)

if __name__=="__main__":
	hangman()
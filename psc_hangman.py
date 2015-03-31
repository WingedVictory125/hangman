import random

def hangman():
#Ask user to enter his/her name
	username = raw_input ("First and Last Name:")
#Create word lists depending on user
	if username == 'Alex Lindo':
		hangman_list = ['koala sucker']
	else:
		hangman_list = ['vanilla', 'two']
#Randomly select a word
	word = random.choice(hangman_list)
#Split the word into letters
	play_word = list(word)
	print play_word
#Store blanks in variable and print
	number_letters = len(play_word)
	blanks = "_"*number_letters
	print "Your word has %d letters:" %(number_letters) + blanks
#Create an empty list that uses the number of letters in the word
	letter_list = []
	for number in range (number_letters):
		letter_list.append(None)
	print letter_list
	ask4letter(letter_list, play_word, blanks)
#Prompt user to guess a letter
#--Check if raw input is valid, else prompt user to give a new letter
def ask4letter(letter_list, play_word, blanks):
	guess_letter = raw_input ("Guess a letter from a to z: ").rstrip()
	valid_letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
	while guess_letter not in valid_letters:
		print "This is not a valid letter."
		guess_letter = raw_input ("Guess a letter from a to z: ").rstrip()
	check_letter(guess_letter, letter_list, play_word, blanks)
#Check if guessed letter is in the play word
#--If guessed letter is in the word --> return blanks w/replaced letters
#--If guessed letter not in word --> check strikes
def check_letter(guess_letter, letter_list, play_word, blanks):	
	for i in range(len(play_word)):
		if guess_letter == play_word[i]:
			blanks = list(blanks)
			blanks[i] = guess_letter
			print "Good guess!"
			print blanks
#-----------This added cummulative guess_letter to list, but didn't add repeat letters
			check_word(blanks, play_word)
			ask4letter(letter_list, play_word, blanks)
		else:
			check_strikes(play_word, guess_letter)
#Did he complete the word? True/False --> End game/Prompt to ask4letter
def check_word(blanks, play_word):
	if blanks == play_word:
		print "You won!"
		#Play again?
		play_again(again, y, n)
#If guessed letter is not in word, create list of wrong letters
def check_strikes(play_word, guess_letter):
	strikes = 7
	wrongLetter = []
	for i in range(7):
		if guess_letter not in play_word: 
			strikes -= 1 #It subtracts 1 form the 7 allotted mistakes
			wrongLetter.append(guess_letter)
			print "Wrong letter! You have %d strikes left." %(strikes) 
			print wrongLetter
			ask4letter(letter_list, play_word, blanks)
			if strikes == 0:
				print "You lost! The word was: "
				print play_word
				#Play again?
def play_again(again, y, n):
	y = True
	n = False
	again = (input("Would you like to go again? [y/n]: "))
	if again == 'y':
		hangman()
	else:
		quit()
#####--What happens if user repeats a letter that was already 
#####--added to guessed blanks/strikes?

#####---What if user wants to play again [y/n]? raw input, again = True
###Draw the hangman:
##Draw the pole
##Draw underscores for each letter in the chosen word
##Draw body parts for each strike (6 strikes max.)

if __name__=="__main__":
	hangman()
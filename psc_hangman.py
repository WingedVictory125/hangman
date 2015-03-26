import random

def hangman():
#Ask user to enter his/her name
	username = raw_input ("First and Last Name:")
#If username is Alex Lindo use list1
	if username == 'Alex Lindo':
		hangman_list = ['koala sucker']
#If user is someone else use list2
	else:
		hangman_list = ['vanilla', 'chocolate', 'strawberry']
#Randomly select a word to use in the first hangman play
	word = random.choice(hangman_list)
#Split the word into letters to use in hangman
#Add each word to the empty list
	play_word = list(word)
	print play_word

#Tell user the number of letters in their word
#Store underscores in variable and print word's blanks
	number_letters = len(play_word)
	blanks = "_"*number_letters
	print "Your word has %d letters:" %(number_letters) + blanks

#Save word in a variable
#Create an empty list that uses the number of letters in the word
	letter_list = []
	for number in range (number_letters):
		letter_list.append(None)
	print letter_list
	ask4letter(letter_list, play_word, blanks)
#Prompt user to guess a letter
def ask4letter(letter_list, play_word, blanks):
	guess_letter = raw_input ("Guess a letter from a to z: ").rstrip()
	valid_letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p' 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
	while guess_letter not in valid_letters:
		print "This is not a valid letter."
		guess_letter = raw_input ("Guess a letter from a to z: ").rstrip()
	check_letter(guess_letter, letter_list, play_word, blanks)

#Create function that checks if the letter is in the play_word
#If the letter given by user is in the word, draw the letter in the corresponding line(s)
#Is the letter in the next space the same? True/False is x==C print letter
#If true print letter and continue the loop until you've gone through all letters
#Check if raw input is valid, else prompt user to give a new letter
#If guessed letter is not in the list, create a list of wrong letters
def check_letter(guess_letter, letter_list, play_word, blanks):	
	for i in range(len(letter_list)):
		if guess_letter == play_word[i]:
			blanks = list(blanks)
			blanks[i] = guess_letter
		else:
			check_errors(play_word, guess_letter, letter_list, blanks)
	print blanks

	#call the function to guess letter
	check_word(blanks, play_word, letter_list)
#Did he complete the word? True/False --> End game/Prompt user for new letter
def check_word(blanks, play_word, letter_list):
	if blanks == play_word:
		print "You won!"
	else:
		ask4letter(letter_list, play_word, blanks)

def check_errors(play_word, guess_letter, letter_list, blanks):
	wrong_letters = []
	if guess_letter not in play_word and len(wrong_letters)<6:
		wrong_letters.append(guess_letter)
	print "Wrong letter!"
	print wrong_letters
	ask4letter(letter_list, play_word, blanks)
			
###Draw the hangman:
##Draw the pole for the hangman
##Draw underscores for each letter in the chosen word
##Else if do strike (draw the head of the hangman)
##Use asterisks for strikes (6)
##If the letter given by the user is not in the word, draw the second body part
##End game if hangman is drawn (6 strokes = 6 errors max.)
##Use strikes in lieu of hangman and o's


if __name__=="__main__":
	hangman()
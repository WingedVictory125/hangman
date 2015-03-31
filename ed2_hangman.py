#Create an empty list that uses the number of letters in the word
	letter_list = []
	for number in range (number_letters):
		letter_list.append(None)
	print letter_list
	ask4letter(number_letters, play_word, blanks)
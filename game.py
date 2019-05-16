class game:
	numberofwords=0
	randWord=""
	status=0
	tempBadGuess=0
	missedLetters=0
	score=0		
		
	def storeValues(self,numberofword,randword,stat,badGuess,missedletters,indiscore):
		self.numberofwords = numberofword
		self.randWord = randword
		self.status = stat
		self.tempBadGuess = badGuess
		self.missedLetters = missedletters
		self.score = indiscore
		return self
		
	def printallObjects(self,finalList,ch):
		print("Game		Word	 Status		Bad Guesses		Missed Letters		Score \n")
		print("\n")
		print("----		----     -----		-----------		--------------		-----"	)
		if(not ch):
			for itemslist in finalList:
				#print(itemslist)
				print(itemslist.numberofwords,"		",itemslist.randWord,"	",itemslist.status,"		",itemslist.tempBadGuess,"			",itemslist.missedLetters,"		",itemslist.score)

		
	
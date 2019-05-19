import random
import game
import stringDatabase;

words=[]
finalresult=[]
finalobjects=[]
numberOfWords=0
finalScore=[]

strData = stringDatabase.stringDatabase()

wordsFrequency={
		'a' : 8.17,
		'b' : 1.49,
		'c' : 2.78,
		'd' : 4.25,
		'e' : 12.70,
		'f' : 2.23,
		'g' : 2.02,
		'h' : 6.09,
		'i' : 6.97,
		'j' : 0.15,
		'k' : 0.77,
		'l' : 4.03,
		'm' : 2.41,
		'n' : 6.75,
		'o' : 7.51,
		'p' : 1.93,
		'q' : 0.10,
		'r' : 5.99,
		's' : 6.33,
		't' : 9.06,
		'u' : 2.76,
		'v' : 0.98,
		'w' : 2.36,
		'x' : 0.15,
		'y' : 1.97,
		'z' : 0.07


		}



class guess():
	'''
		Class Guess To play the Game
	'''

	
	'''def readWords(self):
		"""
			Loading the Words into the List
		"""
		f=open("four_letters.txt")
		if(f.mode == 'r'):
			contents = f.read().replace('\n', ' ')
			global words
			words=contents.split(" ")
			'''
			
	def startPlay(self,contents):
		"""
			Game Begins with the Random Word 
			User has the many choices such as Guess letter Give up and quit.
		"""
		global words
		words=contents.split(" ")
		#print(words)
		global finalScore
		score=0
		randWord=random.choice(words)
		#randWord="defi"
		global numberOfWords
		numberOfWords=numberOfWords+1
		check=True
		tempBadGuess = 0
		missedLetters=0
		status=""
		print("** The great guessing game **")
		print("Current Word ",randWord)
		checkGuess=False
		guessString="----"
		
		while(check):
			print("Current Guess: ",guessString)
			choice=input("g = guess, t = tell me, l for a letter, and q to quit \n")
			if(choice=='g'):
				checkGuess=self.guessingWord(randWord)
				if(checkGuess):
					check=not check	
					status="Success"
					score,lettersuccess=self.calculateScore(guessString,choice,randWord)
					totalLetter=lettersuccess+missedLetters
					if totalLetter != 0:
						score = (score/(totalLetter)) - (tempBadGuess*0.1*score)
					else:
						score = score - (tempBadGuess*0.1*score)
				else:
					tempBadGuess=tempBadGuess+1
			elif(choice=='t'):
				print("The word is ",randWord)
				check=not check
				status="Gave up"
				score,_=self.calculateScore(guessString,choice,randWord)
			elif(choice=='l'):
				guessString,missedLetters=self.showletters(randWord,guessString,missedLetters)
				if(guessString.count('-')==0):
					check=not check
					score=0
					status="Success"
			elif(choice=='q'):
				if(guessString.count('-')==4):
					status="Gave up"
					score,_=self.calculateScore(guessString,choice,randWord)
				print("Thank you for Playing\n")
				check=False

		if(check==False):
			tempGame = game.game()
			#print(" numberOfWords ",numberOfWords ," randWord ",randWord," tempBadGuess ",tempBadGuess, " missedLetters ",missedLetters)
			finalScore.append(score)
			tempGameEntry=tempGame.storeValues(numberOfWords,randWord,status,tempBadGuess,missedLetters,score)
			temp=[numberOfWords,randWord,status,tempBadGuess,missedLetters,score]
			finalresult.append(temp)
			finalobjects.append(tempGameEntry)
			return check
		
			
	def showletters(self,randWord,guessString,missedLetters):
		'''
			Check for Letters Suggested in the Guess Word If yes then the
			Letter is being placed in the string.
			
		'''
	
		letter=input("Enter the Letter\n")
		number=randWord.count(letter)
		print("you found ",number ," letter \n")
		if(number==0):
			missedLetters=missedLetters+1
		temp=list(randWord)
		tempguessString=list(guessString)
		for i in range(len(temp)):
			if(temp[i]==letter):
				tempguessString[i]=letter
		guessString=''.join(tempguessString)
		return guessString,missedLetters
				
	def guessingWord(self,randWord):
		'''
			Checking the Word that is Gussed with the Real word 
			If success return True
			else
			False
			
		'''
		guessWord=input("Enter the Word \n")
		if(guessWord==randWord):
			print("You are Brillant")
			return  True;
		else:
			print("Sorry Bugger!! Please Use your Brain")
			return False;

			
	def calculateScore(self,guessString,choice,randWord):
	
		'''
			To calculate Score
		'''
		
		tempscore=0
		numberofletGuessed=0
		for i in range(len(guessString)):
			if(guessString[i] == "-"):
				tempscore=tempscore+wordsFrequency.get(randWord[i])
			else:
				numberofletGuessed = numberofletGuessed + 1
		if(choice == 't' or choice == 'q'):
			tempscore = -tempscore
		elif(choice == 'g'):
			tempscore = tempscore
		
		return tempscore,numberofletGuessed
			
			
			
	'''def display(self,ch):
		"""
		Display the final Result on the Console
		"""
		print("Game		Word	 Status		Bad Guesses		Missed Letters		Score \n")
		print("\n")
		print("----		----     -----		-----------		--------------		-----"	)
		if(not ch):
			for itemslist in finalresult:
					#print(itemslist)
					print(itemslist[0],"		",itemslist[1],"	",itemslist[2],"		",itemslist[3],"			",itemslist[4],"		",itemslist[5])

		finalAccumulatedScore = sum(finalScore)/len(finalScore)
		print("Final Score: ",finalAccumulatedScore)	'''		
			
if __name__=="__main__":
	"""
	Main Method to Load the Strings into List 
	Display the contents
	"""
	guessob=guess()
	#guessob.readWords()
	contents=strData.readWords()
	ch=guessob.startPlay(contents)
	quit=input("You want to play again(Y/N) \n")
	if(quit=='y' or quit=='Y'):
		ch=True;
	while(ch):
		ch=guessob.startPlay(contents)
		quit=input("You want to play again(Y/N) \n")
		if(quit=='y' or quit=='Y'):
			ch=True
	tempGame = game.game()
	tempGame.printallObjects(finalobjects,ch)
	#guessob.display(ch)
	
				
		
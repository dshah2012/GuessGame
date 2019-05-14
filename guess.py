import random

words=[]
bad_guesses=[]
finalmissedLetters=[]
finalresult=[]
numberOfWords=0


def readWords():
	"""
		Loading the Words into the List
	"""
	f=open("four_letters.txt")
	if(f.mode == 'r'):
		contents = f.read().replace('\n', ' ')
		global words
		words=contents.split(" ")

def startPlay():
	"""
		Game Begins with the Random Word 
	
	"""
	#print(words)
	randWord=random.choice(words)
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
			checkGuess=guess(randWord)
			if(checkGuess):
				check=not check	
				status="Success"
			else:
				tempBadGuess=tempBadGuess+1;
		elif(choice=='t'):
			print("The word is ",randWord)
			check=not check
			status="Gave up"
		elif(choice=='l'):
			guessString,missedLetters=showletters(randWord,guessString,missedLetters)
			if(guessString.count('-')==0):
				check=not check
				status="Success"
		elif(choice=='q'):
			print("Thank you for Playing\n")
			check=False

	if(check==False):
		#print(" numberOfWords ",numberOfWords ," randWord ",randWord," tempBadGuess ",tempBadGuess, " missedLetters ",missedLetters)
		temp=[numberOfWords,randWord,status,tempBadGuess,missedLetters]
		finalresult.append(temp)
		return check
	
		
def showletters(randWord,guessString,missedLetters):
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
	
	
		
	
		
def guess(randWord):
	guessWord=input("Enter the Word \n")
	if(guessWord==randWord):
		print("You are Brillant")
		return  True;
	else:
		return False;
		
		
if __name__=="__main__":
	readWords()
	ch=startPlay()
	quit=input("You want to play again(Y/N) \n")
	if(quit=='y' or quit=='Y'):
		ch=True;
	while(ch):
		ch=startPlay()
		quit=input("You want to play again(Y/N) \n")
		if(quit=='y' or quit=='Y'):
			ch=True
		
	print("Game		Word	 Status		Bad Guesses		Missed Letters		Score \n")
	print("\n")
	print("----		----     -----		-----------		--------------		-----"	)
	if(not ch):
		for itemslist in finalresult:
				#print(itemslist)
				print(itemslist[0],"		",itemslist[1],"	",itemslist[2],"		",itemslist[3],"			",itemslist[4])
				
		
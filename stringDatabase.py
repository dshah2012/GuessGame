class stringDatabase:

	def readWords(self):
		"""
			Loading the Words into the List
		"""
		f=open("four_letters.txt")
		if(f.mode == 'r'):
			contents = f.read().replace('\n', ' ')
			return contents
			
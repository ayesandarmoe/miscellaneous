
# H W I K L
# B C A R F
# T E A R S

# WAR - true
# KITE - false
# CAR - true
# TEARS - true
# TEAR - true
# EAR - true
# EARS - true

puzzle  = [ ['H','W','I','K','L'], ['B','C','A','R','F'], ['T','E','A','R','S']]

def isSame(x,y,idx,word):
	print "inside isSame({},{},{})".format(x,y,idx)	
	if y > len(puzzle[0]) - 1:
		return False
	elif x > len(puzzle) - 1:
		return False
	elif len(word) -1 == idx:
		print puzzle[x][y] == word[idx]
		return puzzle[x][y] == word[idx]
	else:
		isThisLetterSame = puzzle[x][y] == word[idx]
		right = isSame(x, y + 1, idx + 1, word)
		down = isSame(x+1, y, idx+1, word)
		diag = isSame(x + 1, y + 1, idx + 1, word)
		
		return (isThisLetterSame and down)  or (isThisLetterSame and right) or (isThisLetterSame and  diag)

def findWord(puz,word):
	print "Word : {}".format(word)
	numOfRows = len(puz)
	numOfCols = len(puz[0])
	found = False
	for x in range(0,numOfRows):
		for y in range(0, numOfCols):
			print "x: {}, y: {}".format(x,y)
			if puz[x][y] == word[0]: # found first letter
				found = True and isSame(x,y,0,word)	
	print ("==========")
	return found	

assert findWord(puzzle, "CAR") == True
assert findWord(puzzle, "WAR") == True
assert findWord(puzzle, "TEARS") == True
assert findWord(puzzle, "TEAR") == True
assert findWord(puzzle, "CAT") == False
assert findWord(puzzle, "HAT") == False


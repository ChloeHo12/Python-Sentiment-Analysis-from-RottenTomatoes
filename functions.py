# chloe and heidi
# Your functions go here.

def getSentRate(reviewSR):
	"""takes a string containing both a sentiment rating and the associated review text"""
	sentRate = int(reviewSR[0])
	return sentRate

def getRevText(reviewRT):
	"""takes a string containing a sentiment rating and the associated review text"""
	reviewStr = (reviewRT[2:])
	return reviewStr

def cleanText(reviewCT):
	"""takes in a String containing some text and
returns a cleaned up version of the string"""
	rev = reviewCT.lower().strip()
	for char in rev:
		if not char.isalpha() and not char == " ":
			rev = rev.replace(char, "")
	rev = rev.replace("  ", " ")
	return rev

def wordSent(word):
	"""returns the sentiment rating of the word based on all of the reviews in the training.txt file"""
	# search for the word in getRevText
	train = open('training.txt')
	line = train.readline()
	wordCount = 0
	sentTot = 0
	while line:
		rev = getRevText(line)
		cleanLine = cleanText(rev)
		#check if the word is in the clean line
		if word.lower() in cleanLine:
			wordCount += 1
			sentRate = getSentRate(line)
			sentTot += sentRate
		line = train.readline()
	if wordCount == 0:
		return sentTot
	wordAvg = sentTot/wordCount
	return wordAvg

def textSent(text):
	sum = 0 
	count = 0
	for word in text.split():
		wordSentRate = wordSent(word)
		if wordSentRate:
			count += 1
			sum += wordSent(word)
	if count == 0:
		return sum
	else:
		return sum/count









		
	
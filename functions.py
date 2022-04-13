# chloe and heidi
# Your functions go here.
def getSentRate(reviewSR):
	sentRate = int(reviewSR[0])
	return sentRate

def getRevText(reviewRT):
	reviewStr = (reviewRT[2:])
	return reviewStr

def cleanText(reviewCT):
	rev = reviewCT.lower().strip()
	for char in rev:
		if not char.isalpha() and not char == " ":
			rev = rev.replace(char, "")
	rev = rev.replace("  ", " ")
	return rev
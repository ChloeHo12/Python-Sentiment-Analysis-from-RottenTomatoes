# lab09
# chloe and heidi

from functions import *

# #a
# valid = open('validation.txt')
# line = valid.readline()
# print(getSentRate(line))
# print(getRevText(line))

# #b
# rev = getRevText(line)
# #Computer's rating
# print("Computer Sentiment Rating:", textSent(rev))
# #Actual human rating: 1 (negative)
# print("Human Sentiment Rating:", getSentRate(line))

# #c
# lineSentRate = textSent(line)
# lineHumanRate = getSentRate(line)
# sentError = abs(lineSentRate - lineHumanRate)
# print("The error between computed rating and human rating:", sentError)

#d + e
valid = open('validation.txt')
line = valid.readline()
count = 0
lineSentRate = 0
lineHumanRate = 0
errorTot = 0
while line:
	count += 1
	lineSentRate = textSent(line)
	lineHumanRate = getSentRate(line)
	sentError = abs(lineSentRate-lineHumanRate)
	errorTot += sentError
	print("Review", count)
	print("Computer Sentiment Rating:", lineSentRate)
	print("Human Sentiment Rating:", lineHumanRate)
	print("The error between computed rating and human rating:", sentError)
	print("\n")
	line = valid.readline()

errorAvg = errorTot/count
print("The error average:", errorAvg)


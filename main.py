# lab09
# chloe and heidi

from functions import *

#a
valid = open('validation.txt')
line = valid.readline()
# print(getSentRate(line))
# print(getRevText(line))

# #b
# rev = getRevText(line)
# #Computer's rating
# print(textSent(rev))
# #Actual human rating: 1 (negative)
# print(getSentRate(line))

# #c
# lineSentRate = textSent(line)
# lineHumanRate = getSentRate(line)
# sentError = abs(lineSentRate-lineHumanRate)
# print(sentError)

#d
count = 0
lineSentRate = 0
lineHumanRate = 0
while line:
	count += 1
	lineSentRate = textSent(line)
	lineHumanRate = getSentRate(line)
	sentError = abs(lineSentRate-lineHumanRate)
	print("Review", count)
	print("Computer Sentiment Rating:", lineSentRate)
	print("Human Sentiment Rating:", lineHumanRate)
	print("The error between computed rating and human rating:", sentError)
	print("\n")
	line = valid.readline()


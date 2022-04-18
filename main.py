# lab09
# chloe and heidi

from functions import *

#a
valid = open('validation.txt')
line = valid.readline()
print(getSentRate(line))
print(getRevText(line))

#b
rev = getRevText(line)
#Computer's rating
print(textSent(rev))
#Actual human rating: 1 (negative)
print(getSentRate(line))

#c
lineSentRate = textSent(line)
lineHumanRate = getSentRate(line)
sentError = abs(lineSentRate-lineHumanRate)
print(sentError)
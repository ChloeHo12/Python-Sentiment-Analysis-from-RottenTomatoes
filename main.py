# lab09
# chloe and heidi

from functions import *

valid = open('validation.txt')
line = valid.readline()
print(getSentRate(line))
print(getRevText(line))

rev = getRevText(line)
#Computer's rating
print(textSent(rev))
#Actual human rating: 1 (negative)
print(getSentRate(line))

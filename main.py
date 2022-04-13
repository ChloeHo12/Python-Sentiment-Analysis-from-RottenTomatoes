# lab09
# chloe and heidi
from functions import *

train = open('training.txt')
line = train.readline()
count = 0
sentTot = 0
line = train.readline()
while line:
	sentTot += getSentRate(line)
	count = count + 1
	line = train.readline() 
avg = sentTot/count
print("Average sentiment rating:", avg)
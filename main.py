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

train.close()

print(wordSent('politics'))

assert abs(wordSent('politics')) == 0, 'politics is not in review'
assert abs(wordSent('python')) == 0, 'python is not in review'
assert abs(wordSent('Computer')) == 0, 'Computer is not in review'
assert abs(wordSent('Apple')) == 0, 'Apple is not in review'
assert abs(wordSent('Youtube')) == 0, 'Youtube is not in review'
assert abs(wordSent('Bag')) == 0, 'Bag is not in review'
assert abs(wordSent('programming')) == 0, 'programming is not in review'
assert abs(wordSent('science')) == 0, 'science is not in review'
assert abs(wordSent('phone')) == 0, 'phone is not in review'
assert abs(wordSent('physics')) == 0, 'physics is not in review'

print('Success!')
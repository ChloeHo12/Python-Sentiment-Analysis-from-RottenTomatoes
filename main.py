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

assert cleanText('I lauGHed I CrieD')=='i laughed i cried', 'upper case letters'
assert cleanText(' Two ThumBS DowN ')=='two thumbs down', 'spaces at start and end'
assert cleanText(' This "1" wasn`t BAD!!!! ')=='this wasnt bad', 'non alpha chars' 
epsilon = 0.0001
assert abs(wordSent('Fabulous') - 2.75) < epsilon, 'fabulous: wrong SR'
assert abs(wordSent('boring') - 1.1428571428571428) < epsilon,'boring: wrong SR'
assert abs(wordSent('love') - 2.574660633484163) < epsilon, 'love: wrong SR'
assert abs(wordSent('hate') - 1.7954545454545454)< epsilon, 'hate: wrong SR'
assert abs(wordSent('the') - 2.038604742308446) < epsilon, 'the: wrong SR'
#commit for words that do not appear in training.txt
assert (wordSent('biology')) == 0, 'biology: wrong SR'
print('Success!') 
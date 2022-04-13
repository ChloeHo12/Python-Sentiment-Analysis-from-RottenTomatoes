# lab09
# chloe and heidi
from functions import *

train = open('training.txt')
line = train.readline()

print(cleanText(line))

assert cleanText('I lauGHed I CrieD')=='i laughed i cried', 'upper case letters'
assert cleanText(' Two ThumBS DowN ')=='two thumbs down', 'spaces at start and end'
assert cleanText(' This "1" wasn`t BAD!!!! ')=='this wasnt bad', 'non alpha chars'
print('Success!') 



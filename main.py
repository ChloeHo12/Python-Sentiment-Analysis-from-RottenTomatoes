# lab09
# chloe and heidi
from functions import *

train = open('training.txt')
line = train.readline()

print(getSentRate(line))

assert getSentRate('4 I laughed, I cried, it was better than cats.') == 4
'sentiment should be 4'
assert getSentRate('0 Two thumbs down.') == 0, 'sentiment should be 0'
print("Success!") 



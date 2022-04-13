# lab09
# chloe and heidi
from functions import *

train = open('training.txt')
line = train.readline()

print(getRevText(line))

assert getRevText('4 I laughed, I cried, it was better than cats.') == "I laughed, I cried, it was better than cats.", "Review Text should be 'I laughed, I cried, it was better than cats.'" == "I laughed, I cried, it was better than cats."
assert getRevText('0 Two thumbs down.') == 'Two thumbs down.', "Review Text should be 'Two thumbs down.'"
print("Success!") 



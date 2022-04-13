# lab09
# chloe and heidi

train = open('validation.txt')
count = 0
line = train.readline()
while line:
	count = count + 1
	line = train.readline()
train.close()
print('validation.txt has ' + str(count) + ' lines.') 

# A. How many lines are in the training data set?
	# there are 8427 lines in the training data set.

# B. How many lines are in the validation data set?
	# there are 101 lines in the training data set.

# C. Based on the behavior of your program, what value does the .readline() method return when all of the lines in the file have been read? That is, what is the value of line that causes the while loop to terminate?
	# It returns a value of False since it has no data to be passed through it, which allows the while loop to be escaped
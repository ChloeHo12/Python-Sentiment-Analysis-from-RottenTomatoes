# lab09
# chloe and heidi

datafile = open("training.txt")
trainStr = datafile.readline()
print(trainStr)

datafile = datafile.close()
#When we run the program multiple times, the program still prints the first line.
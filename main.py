# lab09
# chloe and heidi
from functions import *

userText = input('Enter the text that you want to know the sentiment rating >> ')
userSent = textSent(userText)
if userSent >= 2:
	print("The sentiment rating is", userSent,". This is positive :)")
else:
	print("The sentiment rating is", userSent, ". This is negative :(")

# 1. What are some phrases you tried where the program got the sentiment category right?
	# love you: positive
	# fabulous movie: positive
	# this movie is great: positive
	# i hate the movie: negative
	# this is a bad movie: negative
	# I wanted to fall asleep: negative
# 2. What is one where it got it wrong?
	# I wanted to love the movie but I did not: positive but should have been negative
	# the movie is more interested in entertaining itself than in amusing us: positive but should have been negative
	# i liked the popcorn but not the movie: positive but should have been negative
# 3. Why does it interpret the sentiment category of certain phrases incorrectly?
	# They may use positive words even though their rating is negative.
	# Computer doesn't understand sarcasm or irony


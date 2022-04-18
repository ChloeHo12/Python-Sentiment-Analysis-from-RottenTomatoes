# lab09
# chloe and heidi
from functions import *

userText = input('Enter the text that you want to know the sentiment rating >> ')
userSent = textSent(userText)
if userSent >= 2.31:
	print("The sentiment rating is", userSent,". This is highly positive :):)")
elif 2.19 <= userSent < 2.31:
	print("The sentiment rating is", userSent,". This is positive :)")
elif 1.8 <= userSent < 2.19:
	print("The sentiment rating is", userSent,". This is neutral. :|")
elif 1.6 <= userSent < 1.8:
	print("The sentiment rating is", userSent,". This is negative :(.")
else:
	print("The sentiment rating is", userSent, ". This is highly negative :(:(")


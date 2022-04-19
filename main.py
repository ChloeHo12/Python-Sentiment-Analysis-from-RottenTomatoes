# lab09
# chloe and heidi
from functions import *

userText = input('Enter the text that you want to know the sentiment rating >> ')
userSent = textSent(userText)
print(userSent)
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

assert 2.19 <= abs(textSent("fabulous movie")) < 2.31, "'fabulous movie' is positive"
assert 1.8 <= abs(textSent("This movie is fine")) < 2.19, "'This movie is fine' is neutral"
assert 1.6 <= abs(textSent("The movie is boring")) < 1.8, "'The movie is boring' is negative"
assert abs(textSent("Terrible movie")) < 1.6, "'Terrible movie' is highly negative"
print('Success')
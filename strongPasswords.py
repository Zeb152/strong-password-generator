import random as r
import pyperclip as pc

lowerLetters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
upperLetters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
specialChar = ['!', '@', '#', '$', '%', '&', '?']

pwLength = 15
timesRun = 0

password = ""

for i in range(pwLength):
    if timesRun == 5:
        password = password + "-"
    if timesRun == 10:
        password = password + "-"

    group = r.randrange(1, 5)
    if group == 1:
        charChoice = r.choice(lowerLetters)
        password = password + charChoice
    if group == 2:
        charChoice = r.choice(upperLetters)
        password = password + charChoice
    if group == 3:
        charChoice = r.choice(numbers)
        password = password + charChoice
    if group == 4:
        charChoice = r.choice(specialChar)
        password = password + charChoice

    timesRun = timesRun + 1

print(password)

pc.copy(password)

#FINAL PASSWORD: xxxxx-xxxxx-xxxxx
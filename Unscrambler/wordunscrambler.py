# Python file that reads a JSON file with words and their lengths and 
# unscrambles user input words

import os
import sys
import json

from collections import Counter

# Get current path of the JSON file
dictionaryFilePath = os.path.realpath("dictionary.json")

# Add some color to life
class color:
    SUCCESS = '\033[92m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'

with open(dictionaryFilePath) as fp:
    wordsDictionary = json.load(fp)

inputWord = input("Enter a word: ").lower() # Work only with lowercase words
inputWordCounts = Counter(inputWord)
inputWordLength = len(inputWord)

# Error check
if inputWordLength == 0 or not inputWord.isalpha():
    sys.exit(color.FAIL + "No word entered or input is not a word" + color.ENDC)

# Create a list of words with same length as the user input word
wordsList = wordsDictionary[str(inputWordLength)]

gotResult = False
firstTime = True

# Print all words that can be formed with the same letters as in user input word
# or in other words, unscramble!!
for word in wordsList:
    if Counter(word) == inputWordCounts:
        if firstTime:
            print("Unscrambled word(s) is/are : ")
            firstTime = False
        print(color.SUCCESS + word + color.ENDC + " ")
        gotResult = True

if not gotResult:
    print(color.FAIL + "Unable to unscramble word" + color.ENDC)
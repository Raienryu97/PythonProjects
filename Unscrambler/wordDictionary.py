# Python file that creates a JSON file with keys as the lengths of words
# and value as a list of the words themselves. It uses a textfile "words.txt" as 
# the input ( Source of words.txt : https://svnweb.freebsd.org/csrg/share/dict/ )

import os
import json

# Get current path of the words file
wordsFilePath = os.path.realpath("words.txt")
# Initialise variables
wordsDictionary = dict()
tempWordsList = []
wordsList = []

with open(wordsFilePath) as fp:
    tempWordsList = list(fp)

# Remove the '\n' that was read in with the list() command
wordsList = [word.strip('\n') for word in tempWordsList]

# Create the dictionary with key as the length of the word
# and the words themselves in a list as the value
# Example {"1" : ['a','b','c',...]}
for i in range(len(wordsList)):
    currentWordLength = len(wordsList[i])
    if currentWordLength in wordsDictionary:
        wordsDictionary[currentWordLength].append(wordsList[i])
    else:
        wordsDictionary[currentWordLength] = [wordsList[i]]

# Store the dictionary in a JSON file
with open('dictionary.json','w') as fp:
    json.dump(wordsDictionary, fp)
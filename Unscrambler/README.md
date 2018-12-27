# Word Unscrambler
Python implementation of a word unscrambler. It takes a scrambled word as input and returns as many meaningful words as possible.

## Implementation
The basic implementation was based around the idea of python's dictionary. We create a dictionary that has keys as the length of the word and the words as a list.
```python
# Sample of how the dictionary looks
dict1 =  {"1" : ['a','b','c',...], "2" : ['aa','ab',...]} 
````

Creating the dictionary is done by the [wordDictionary.py file](wordDictionary.py)
which reads the [words.txt](words.txt) file, processes it and stores it as a JSON.

The second file [wordunscrambler.py](wordunscrambler.py) loads the created [dictionary.json](dictionary.json) file and searches in it.

We find the length of the user input word and get all the words of the same length from a stored dictionary and keep searching for words with same letter count. This is achieved by using the method `Counter` from `collections`.

```bash
# Sample of how Counter works
>>> from collections import Counter
>>> print(Counter("word"))
Counter({'w': 1, 'o': 1, 'r': 1, 'd': 1})
```

## Usage
SInce this repo already has the dictionary.json, you only need to clone this repo and run `python3 wordunscrambler.py` on your terminal. The following is a sample execution.
```bash
$ python3 wordunscrambler.py 
Enter a word: ilstne
Unscrambled word(s) is/are : 
listen 
silent 
tinsel 
```


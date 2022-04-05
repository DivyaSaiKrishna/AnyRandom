import random

class wordSelector:
    def __init__(self, wordList, wordsSeparator):
        self.wordList = wordList
        self.wordSeparator = wordsSeparator
        
    def getWord(wordList,wordsSeparator):
        return wordList[random.randint(0, len(wordList) - 1)]

   
###############################################################################    
# Random Word Selector slects random word from a list of words
# 
# Input : 
#       wordList : abcd, awer, qwert, erwerwe, wrwqe 
#       wordsSeparator : ,
#       word : awer
#           or 
#   wordList : abcd, awer, qwert, erwerwe, wrwqe 
#       wordsSeparator : 
#       word : qwert
# 
#  Returns:  
#   String : A random word from the word list.
################################################################################
    

import random
class wordSelector:
    def __init__(self, wordList, wordsSeparator):
        self.wordList = wordList
        self.wordSeparator = wordsSeparator
        
    def getWord(self):
        if(self.wordSeparator != ''):
            return self.wordList[random.randint(0, len(self.wordList)-1)].split(self.wordSeparator)
        return self.wordList[random.randint(0, len(self.wordList) - 1)].split(' ')

   

import random


class randomSequenceGenerator:
    def __init__(self, length):
        self.length = length
        self.sequence = []
        self.rset = {''}
        self.generate()
        
    def generate(self):
        for i in range(self.length):
            randomNumber = random.randint(0, self.length - 1)
            if not randomNumber in self.rset:
                self.rset.add(int(randomNumber))
                self.sequence.append(randomNumber)
        
        if(len(self.sequence) == self.length):
            return self.sequence
        else :
            self.generate()
    
        

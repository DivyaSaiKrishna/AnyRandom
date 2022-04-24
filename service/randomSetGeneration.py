

import random

from flask import jsonify


class randomSetGeneration:
    def __init__(self,numofsets,numofunq,rangeMax,rangeMin):
        self.numofsets = int(numofsets)
        self.numofunq = int(numofunq)
        self.rangeMax = int(rangeMax)
        self.rangeMin = int(rangeMin)
        self.setofsets =[]
        self.settoadd = []
        self.sequence = []
        self.rset = {''}
        self.generate()
    
    def geneRSets(self):
        for i in range(self.numofsets):
            self.settoadd.append(randomSetGeneration.generate())
        return jsonify(self.settoadd)
        
    def generate(self):
            for i in range(self.numofunq):
                randomNumber = random.randint(self.rangeMin, self.rangeMax-1)
                if not randomNumber in self.rset:
                    self.rset.add(int(randomNumber))
                    self.settoadd.append(randomNumber)
        
            if(len(self.settoadd) == self.numofunq):
                print('in fi',self.settoadd)
                self.sequence = self.settoadd
                self.settoadd.clear()
                return self.sequence
            else :
                print('in else',self.settoadd)
                self.generate()
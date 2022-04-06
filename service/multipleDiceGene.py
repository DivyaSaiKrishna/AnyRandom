

import random

from flask import jsonify


class multipleDiceGene:
    def __init__(self,num):
        self.num = num
        self.dice = []
    
    def geneMDice(self):
        for i in range(self.num):
            self.dice.append(random.randint(1,6))
        return jsonify(self.dice) 
    
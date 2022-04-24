

import random

from flask import jsonify


class pyRandom:
    def __init__(self,num):
        self.num = int(num)
    
    def randomCheck(self):
        listran =[]
        for i in range(self.num):
            randNu = random.random()
            listran.append(randNu)
        return jsonify(listran)
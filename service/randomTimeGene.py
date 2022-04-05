
import random


class randomTimeGene:
    def __init__(self,type):
        self.type = type
        
    def genTime(type):
        if type == "24":
            return str(random.randint(0,23)) + ":" + str(random.randint(0,59)) + ":" + str(random.randint(0,59)) 
        elif type == "12":
            return str(random.randint(1,12)) + ":" + str(random.randint(0,59)) + ":" + str(random.randint(0,59)) 
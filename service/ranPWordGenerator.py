######################################################################
#  Custom Password Generator Service
#
#   This service generates a random password.
#   
#   Returns:  
#   String : returns a random password build by using special characters,greek symbols & roman.
######################################################################

import random


class ranPWordGenerator:
    def __init__(self,length,type):
        self.alphabet =  "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
        self.specialchar = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()_+-=[]}{|;':,./<>?`~"
        self.greeksymbol = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()_+-=[]}{|;':,./<>?`~αβζδπΨ"
        self.roman = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()_+-=[]}{|;':,./<>?`~αβζδπΨIVXLCDM"
        self.length = length
        self.type = type
    
    def generate(self):
        if self.type == "simple":
            return ''.join(random.choice(self.alphabet) for i in range(self.length))
        elif self.type == "strong":
            return ''.join(random.choice(self.specialchar) for i in range(self.length))
        elif self.type == "hard" :
            return ''.join(random.choice(self.greeksymbol) for i in range(self.length))
        elif self.type == "veryhard" :
            return ''.join(random.choice(self.roman) for i in range(self.length))
        else:
            return ''.join(random.choice(self.alphabet) for i in range(self.length))
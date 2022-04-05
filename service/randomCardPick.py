
import random

class randomCardPick:
    def __init__(self):
        self.type = ["♣","♦","♥","♠"]
        self.card = ["A","2","3","4","5","6","7","8","9","10","J","Q","K","Joker"]
        
    def pick(self):
        card = self.card[random.randint(0,13)]
        if card == "Joker":
            return card 
        return self.type[random.randint(0,3)] + " " + card
    
    def pickNum(self, num):
        sequenceLi = []
        for i in range(num):
            sequenceLi.append(self.pick())
        return str(sequenceLi)
    
    
    
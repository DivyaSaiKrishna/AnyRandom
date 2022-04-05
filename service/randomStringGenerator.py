import random

class randomStringGenerator:
    def __init__(self,length):
        self.alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
        self.length = length

    def generate(self):
        return ''.join(random.choice(self.alphabet) for i in range(self.length))
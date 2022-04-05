import random
class NumberGenerator:
    def __init__(self, min, max):
        self.min = min
        self.max = max
      
    def randomNumber(min,max):
        try:
          if(max > min):
                return random.randint(min , max)
          return random.randint(max, min)
        except Exception as e:
          print(e)
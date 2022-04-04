import random

from app import randomNumber


class NumberGenerator:
    def randomNumber(self, min, max):
        return random.randint(min, max)
    
        
        
        
            
## throws Exception:
      ##  try:
        ##    if(min > max):
         ##       raise Exception("Min value is greater than max value")
      ##      else:
            ##    return random.randint(min, max)
       ## except Exception as e:
        ##    print(e)*/  
       ## 

from distutils.log import debug
from numpy import int64
import math


class myRandom:
    def __init__(self):
        self.seed = float(0.218700)
        
    def myrandom(self,num):
        self.num =num
        if(self.num > 9223372036854775807 or self.num < -9223372036854775808):
            print("num is out of range",self.num)
            frac, whole = math.modf(self.num)
            res = round(frac,8)
        else:
            print("num is in range",self.num)
            temp = (4/3)*(math.pi)*((self.num)*(self.num)*(self.num)) 
            res, whole = math.modf(temp)
        return round(res,8)
            
    def cycle(self,num):
        randList = []
        randNum = self.myrandom(float(num))
        randList.append(randNum)
        for i in range(10):
            randNum = self.myrandom(float(randNum))
            print(randNum)
            randList.append(randNum)
        return str(randList)
                
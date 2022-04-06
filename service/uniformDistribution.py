"""A continuous random variable X
X is said to have a Uniform distribution over the interval [a,b][a,b]
, shown as X∼Uniform(a,b)
X∼Uniform(a,b) , where a and b are the lower and upper limits of the
fX(x)={1/b−a 0 } a<x<b -  x<a or x>b"""

import random


class uniformDistribution:
    def __init__(self, min, max):
        self.min = min
        self.max = max

    def get_min(self):
        return self.min

    def get_max(self):
        return self.max
    #"Get a random number in the range [a, b) or [a, b] depending on rounding."
    def get_uniformDistr(self):
        self.min + ((self.max - self.min) * random.random())
        
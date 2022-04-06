import random

from math import log as _log, exp as _exp, pi as _pi, e as _e, ceil as _ceil
from math import acos as _acos, cos as _cos, sin as _sin
from math import tau as TWOPI, floor as _floor

from service.squareRoot import mySquareRoot


class gaussionRandomNumber:
    def __init__(self, mean, std):
        self.mean = mean
        self.std = std
        self.random = random.Random()
        self.random.seed()
        self.gauss_next = None

    def getRandomNumber(self):    
        random = self.random
        z = self.gauss_next
        self.gauss_next = None
        if z is None:
            x2pi = random.random() * float(TWOPI)
            g2rad = mySquareRoot(-2.0 * _log(1.0 - random.random())).squareRoot()
            z = _cos(x2pi) * float(g2rad)
            self.gauss_next = _sin(x2pi) * float(g2rad)

        return str(self.mean + z * self.std)
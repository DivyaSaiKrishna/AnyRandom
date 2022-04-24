######################################################################
#  Custom Square Root Service
#
#   This service computes the square root of a given number.
#   The service is implemented by using Binary Search.
#   
#
#   Returns:  
#   Integer : Square root of the given number.
######################################################################

class mySquareRoot:
    def __init__(self,number):
        self.first = 1
        self.res = -1
        self.number = number
        self.last = number

    def squareRoot(self):
        if(int(self.number) < 0):
            return -1
        elif(int(self.number) == 0):
            return 0
        while(int(self.first)<=int(self.last)):
            mid = (int(self.first)+(int(self.last)-int(self.first))/2)
            if(int(self.number)%int(mid) ==0 and int(self.number)/int(mid)==int(mid)):
                self.res = mid
                break
            if(int(mid)<=int(self.number)/int(mid)):
                self.res=mid
                self.first = mid+1
            else:
                self.last = mid-1
                
        return float(self.res)
        
import random

class randomDateGenerator:
    def __init__(self):
        self.date = self.getRandomDate()
        
    def getRandomDate(self):
        year = random.randint(1800,7000)
        month = random.randint(1,12)
        if(month == 2):
            day=random.randint(1,28)
        elif(month == 4 or month == 6 or month == 9 or month == 11):
            day=random.randint(1,30)
        elif(month ==2 and year%4 == 0):
            day=random.randint(1,29)
        else:
            day = random.randint(1,31)
        return str(year) + "/" + str(month) + "/" + str(day)
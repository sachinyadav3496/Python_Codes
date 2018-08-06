class Calendar(object):
    months = (31,28,31,30,31,30,31,31,30,31,30,31)
    def __init__(self, day=1,month=1,year=1900):
        self.__day = day
        self.__month = month
        self.__year = year
    def leapyear(self,y):
        if y % 4 :
            return 0
        else:
            if y % 400:
                return 0
            else:
                return 1
    def set(self,day,month,year):
        self.__day = day
        self.__month = month
        self.__year = year
    def get(self):
        return (self,self.__day,self.__month,self.__year)
    def advance(self):
        months = Calendar.months
        max_days = months[self.__month-1]
        if self.__month == 2 :
            max_days += self.leapyear(self.__year)
        if self.__day == max_days:
            self.__day = 1
            if (self.__month == 12):
                self.__month = 1
                self.__year += 1 
            else:
                self.__month += 1
        else:
            self.__day += 1
    def __str__(self):
        return str(self.__day)+"/"+str(self.__month)+"/"+str(self.__year)
y = Calendar()
print(y)
y.advance()
print(y)


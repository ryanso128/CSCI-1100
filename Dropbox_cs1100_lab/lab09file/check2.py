'''
Start to the Date class for Lab 9.  This code will not run in Python
until three methods are added:
    __init__,
    __str__
    same_day_in_year
'''

days_in_month = [ 0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31 ]
month_names = [ '', 'January', 'February', 'March', 'April', 'May', 'June', 'July',\
                    'August','September', 'October', 'November', 'December' ]

class Date(object):
    def __init__(self, year0=1900, month0=1, day0=1):
        self.year=year0
        self.month=month0
        self.day=day0
        
    def __str__(self):
        return '{}/{}/{}'.format(self.year, self.month, self.day)
    
    def same_day_in_year(obj1, obj2):
        if obj1.month==obj2.month and obj1.day==obj2.day:
            return True
        return False
    
    def leap_year(self):
        if (self.year%4==0 and not self.year%100==0) or self.year%400==0:
            return True
        return False
    
    def __lt__(obj1, obj2):
        if obj1.year<obj2.year:
            return True
        if obj1.year==obj2.year and obj1.month==obj2.month:
            return obj1.day<obj2.day
        if obj1.year==obj2.year:
            return obj1.month<obj2.month
        return False
        
        


if __name__ == "__main__":
    d1 = Date(1972, 3, 27)
    d2 = Date(2000, 3, 13)
    d3 = Date(1900, 4, 13)
    print("d1: " + str(d1))
    print("d2: " + str(d2))
    print("d3: " + str(d3))
    print("d1.same_day_in_year(d2)", d1.same_day_in_year(d2))
    print("d2.same_day_in_year(d3)", d2.same_day_in_year(d3)) 
    print(Date.leap_year(d3))
    print(d2<d3)

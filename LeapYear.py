def Leap_Year(year):
     c1 = (year % 4 == 0)
     c2 = (year % 100 != 0)
     c3 = (year % 400 == 0)
    
     if (c1 and c2) or c3:
        return True
     else:
        return False 
def Leap_Year(year):
    c1 = (year % 4 == 0)
    c2 = (year % 100 == 0)
    c3 = (year % 400 == 0)
 
    if c1:
        if c2:
            if c3:
                return True
            return False
        return True
    return False
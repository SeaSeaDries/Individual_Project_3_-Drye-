from LeapYear import Leap_Year

#Commet: This test passes 100% statement coverage but the false outcomes of my if statements have not been tested thus not 100% condition coverage

def tests():
    assert Leap_Year(1600) == True, "Test failed: 1600 should be a leap year"

    print("All tests passed")

tests()
from LeapYear import Leap_Year

#Comment: these tests pass 100% Condition coverage but wont be able to do 1600, 2000, or 2400 and so forth. So no statement coverage

def tests():
    
    # Test case 1: Leap year
    assert Leap_Year(2024) == True, "Test failed: 2024 is a leap year"
    
    # Test case 2: Not Leap year
    assert Leap_Year(1900) == False, "Test failed: 1900 is not a leap year"
    
    # Test case 3: Not Leap year
    assert Leap_Year(2023) == False, "Test failed: 2023 is not a leap year"
    
    print("All tests passed - Condition Coverage")

tests()
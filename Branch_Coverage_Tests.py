from LeapYear import Leap_Year

#Comment: These Tests pass Branch Coverage but not the other ones because 400 is never true so it's incomplete

def tests():
    print("Running Branch_Coverage_Tests...")
    
    # Test case 1: True Branch
    assert Leap_Year(2024) is True, "Test failed: 2024 is a leap year"
    
    # Test case 2: False Branch
    assert Leap_Year(1900) is False, "Test failed: 1900 is not a leap year"
    
    print("All tests passed - Branch Coverage")

tests()
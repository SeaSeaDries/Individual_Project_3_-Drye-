from LeapYear import Leap_Year

#Comment: These tests are 100% for Branch and Condition but not MC/DC because condition c1 does not have an independence pair

def tests():
    print("Running Branch_And_Condition_Coverage_Tests...")
    
    assert Leap_Year(2024) is True, "Test failed: 2024 is a leap year"

    assert Leap_Year(2000) is True, "Test failed: 2000 is a leap year"

    assert Leap_Year(1900) is False, "Test failed: 1900 is not a leap year"

    assert Leap_Year(2023) is False, "Test failed: 2023 is not a leap year"
    
    print("All tests passed - Branch and Condition Coverage")

tests()
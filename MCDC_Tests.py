from LeapYear import Leap_Year

#Comment: These tests achieves 100% MC/DC using 4 test cases because every condition (c1, c2, c3) has been shown to independently affect the decision outcome.

def tests():
    print("Running MCDC_Tests...")
    
    assert Leap_Year(2024) is True, "Test failed: 2024 is a leap year (c1=T, c2=T, c3=F)"

    assert Leap_Year(1900) is False, "Test failed: 1900 is not a leap year (c1=T, c2=F, c3=F)"

    assert Leap_Year(2023) is False, "Test failed: 2023 is not a leap year (c1=F, c2=T, c3=F)"

    assert Leap_Year(2000) is True, "Test failed: 2000 is a leap year (c1=T, c2=F, c3=T)"
    
    print("All tests passed - MC/DC Coverage")

tests()
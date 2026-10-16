from LeapYear import Leap_Year

def tests():

    assert Leap_Year(2024) is True, "Failed Combination 1 (2024)"

    assert Leap_Year(1900) is False, "Failed Combination 2 (1900)"

    assert Leap_Year(2000) is True, "Failed Combination 3 (2000)"

    assert Leap_Year(2023) is False, "Failed Combination 4 (2023)"

    print("All tests passed - Multiple Conditions Coverage")

tests()


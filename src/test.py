#!/usr/bin/env python

from cat_controller import CatController

WATER_HOURS = [8, 9, 10, 11, 13, 14, 15, 16, 17, 18, 19]


def main():
    test_failed = False
    cat_controller = CatController()

    # Test that water is only given each hour 8-11 and 13-19.
    for hour in range(0, 23):
        if hour in WATER_HOURS:
            if "Give water." not in cat_controller.hourly_run(hour):
                test_failed = True
                print(f"Test failed: Expected to give water at {hour}, but it didn't.")
        elif "Give water." in cat_controller.hourly_run(hour):
            test_failed = True
            print(f"Test failed: Expected not to give water at {hour}, but it did.")

    # Test that cat cage is opened at 7:
    if "Open cat cage." not in cat_controller.hourly_run(7):
        test_failed = True
        print("Test failed: Expected to open cat cage at 7, but it didn't.")

    # Test that cat cage is closed at 20:
    if "Close the cage." not in cat_controller.hourly_run(20):
        test_failed = True
        print("Test failed: Expected to close cat cage at 20, but it didn't.")

    # Test that cat is fed at 8, 12, and 17 with specific foods:
    for hour in [8, 12, 17]:
        hour_status = cat_controller.hourly_run(hour)
        expected_foods = ["1 mouse", "1 hamster", "1 chicken"]
        for food in expected_foods:
            if food not in hour_status:
                test_failed = True
                print(f"Test failed: Expected {food} to be fed at {hour}, but it wasn't.")

    if test_failed:
        print("Unfortunately, one or several tests failed.")
    else:
        print("All tests ran successfully.")


if __name__ == "__main__":
    main()

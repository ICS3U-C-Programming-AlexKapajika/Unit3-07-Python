#!/usr/bin/env python3
# Created by: Alex Kapajika
# Created on: Oct 26, 2023
# This program ask the user for his age and calculate if your age is valid to date
# her grandchild


def main():
    # Getting the user age as a string
    user_age_str = input("How old are you? : ")
    print("")

    # Try and catching no valid age
    try:
        user_age_int = int(user_age_str)
        # Comparing the user age to the requirement to date her
        if user_age_int > 25 and user_age_int < 40:
            print("You are old enough to date her.")
        elif user_age_int < 0 or user_age_int > 120:
            print("This is not a valid age.")
        elif user_age_int > 40 or user_age_int < 25:
            print("You can't date her")

    except Exception:
        print("This is not a valid age")


if __name__ == "__main__":
    main()

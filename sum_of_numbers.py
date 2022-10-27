#!/usr/bin/env python3
# Created By: Jeremiah Omoike
# Date: October 19 2022
# This program asks the user to enter a positive number
# and then uses a loop to calculate and display the sum
# of all numbers looped from 0 until that number.


def main():
    # set a variable for the loop counter and sum to zero
    loop_counter = 0
    sum = 0

    # input
    # get user number as a string
    user_number_as_string = input("Enter a positive number: ")
    print("")
    # Tries to convert the user input as string to an int.Ends and loops the program if user did not input an integer
    try:
        user_number_as_int = int(user_number_as_string)

    except Exception:
        print()
        print("Please input a positive integer.")
        return main()
    if user_number_as_int < 0:
        print("Please input a positive integer.")
    else:
        # process
        # Tracks the amount of loops. The tracking stops when the amount of loops is equal to the user input
        while loop_counter <= user_number_as_int:
    # output
    #  Tracks and displays The amount of times that the program loops
            print("")
            print("Tracking {0} times through loop.".format(loop_counter))
            loop_counter = loop_counter + 1
    # calculate the sum of all numbers from 0 to user number
    sum = sum + loop_counter
# output
# Displays the sum of numbers looped from 0 to the user input
    print("")
    print("The sum of the numbers from 0 to {} is: {}.".format(user_number_as_int, sum))


if __name__ == "__main__":
    main()

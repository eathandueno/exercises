#!/usr/bin/env python3

# display a welcome message
print("The Miles Per Gallon program")
print()
while True:
# get input from the user
    miles_driven = float(input("Enter miles driven:         "))
    gallons_used = float(input("Enter gallons of gas used:  "))
    cost_per_gallon = float(input("Enter cost per gallon:       "))
    if miles_driven <= 0:
        print("Miles driven must be greater than zero. Please try again.")
    elif gallons_used <= 0:
        print("Gallons used must be greater than zero. Please try again.")
    elif cost_per_gallon <= 0:
        print("Cost per gallon must be greater than zero. Please try again.")
    else:
        # calculate and display miles per gallon
        mpg = round(miles_driven / gallons_used, 2)
        print("Miles Per Gallon:          ", mpg)

        choice = input("Get entries for another trip? (y/n): ")
        if choice.lower() != "y":
            break
        else:
            continue


print()
print("Bye!")




#!/usr/bin/env python3

# display a welcome message
print("The Miles Per Gallon program")
print()

# get input from the user
miles_driven= float(input("Enter miles driven:\t\t"))
gallons_used = float(input("Enter gallons of gas used:\t"))
cost_per_gallon = float(input("Enter cost per gallon:\t\t"))
# calculate miles per gallon
mpg = round((miles_driven / gallons_used),1)
# calculate total gas cost
total_gas_cost = round((gallons_used * cost_per_gallon),2)
            
# format and display the result
print(f"Miles Per Gallon:\t\t{mpg}")
print(f"Total Gas Cost:\t\t\t${total_gas_cost}")
print()
print("Bye!")



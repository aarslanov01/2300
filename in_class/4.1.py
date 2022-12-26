'''
Gallons per Pound per Mile
'''
# using the float to constraint the output to float numbers
miles = float(input("Please enter the miles driven: "))
gallons = float(input("Please enter the gallons of gas used: "))
weight = float(input("Please enter your weight: "))

# gallons per pound per miles should be the formula below
usage = gallons/weight/miles

print(f'\nYour total Gallons per Pound per Mile is: {usage}')

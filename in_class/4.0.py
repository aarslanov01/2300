'''
Calculate the KPG
'''

# using the float to constraint the output to float numbers
miles = float(input("Please enter the miles driven: "))
gallons = float(input("Please enter the gallons of gas used: "))

# using the formula below to convert the miles into kilometers
kilometers = miles * 1.6

kpg = kilometers / gallons 

print(f'\nYour total KPG is: {kpg}')


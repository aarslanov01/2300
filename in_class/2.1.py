'''
Write a program that asks the user for a number in the range of 1 through 7. The program should display the corresponding day of the week, 
where 1 = Monday, 2 = Tuesday, 3 = Wednesday, 4 = Thursday, 5 = Friday, 6 = Saturday, and 7 = Sunday. The program should display an error 
message if the user enters a number that is outside the range of 1 through 7.
'''

# we set the input as an integer to prevent the error
number = int(input('please enter a number in the range 1 - 7: '))

# start the required logic
if number == 1:
    print('monday')
    
elif number == 2:
    print('tuesday')
    
elif number == 3:
    print('wednesday')

elif number == 4:
    print('thursday')

elif number == 5:
    print('friday')

elif number == 6:
    print('saturday')

elif number == 7:
    print('sunday')

# check the input against the constraint
else:
    print('the number should be within range 1 to 7')

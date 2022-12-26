'''
Ask the user if they are hungry and request the response to be single character as y/n or Y/N. If they are hungry, inform them of your favorite restaurant otherwise inform them to go back to work!
'''

# I will convert  both inputs (Y or y) to the lower case for the sake of convenience
hungerState = input('Are you hungry? Please input (y/n) or (Y/N)').lower()

# account the logic for converted lower case
if hungerState == 'y':
    print('my favorite restaurant is: Benihana')
    
elif hungerState == 'n':
    print('go back to work')

else: 
    print('please input (y/n) or (Y/N)')

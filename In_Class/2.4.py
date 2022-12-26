
'''
`Password verification: Ask user to enter a password and compare the user entered value to this value: quadrivium. If the user entered value matches this value then inform the user 
“Correct password” otherwise inform the user “Incorrect Password”

'''
# account the input for upper and lower cases
password = input('please enter the password:')

# set the true password
passwordCheck = 'quadrivium'

# set the logic
if password == passwordCheck:
    print('Correct password')

else: 
    print('Incorrect Password')

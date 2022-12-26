'''
Write a program to input a number. Then, allow the user to guess up to 5 times what the number is.
'''

# lets thake an input
number = float(input('please input a number: '))

# create the counter to compare the loop against
counter = 0

while True and counter <=5:
    # add the number to the counter till it == 5
    counter += 1
    check_number = float(input('what is the number? '))
    
    if check_number == number:
        print('good job, number is found')
        break
        
    else:
        print('no number')

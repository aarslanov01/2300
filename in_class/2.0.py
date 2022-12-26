'''
Write a program that decides whether airline passengers have to pay excess baggage fees. Ask the user how much their bag weighs. 
If the bag weighs more than 50lbs then feesCharged should be $25 and inform the user as such. Otherwise inform the user that "Good job of packing light!"
'''

# we set the input as float to make sure the input is a digit
weight = float(input("how much does your bag weighs?: ")) 

# set the counter of fees
feesCharged = 0


if weight > 50:
    feesCharged += 25 
    print(f'fees charged: {feesCharged}')
else:
    print('good job of packing light!')

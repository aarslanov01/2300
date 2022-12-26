'''
Write a program for a vending machine that allows the user to insert up to $5 in coins and bills. 
While the user is entering money, display the total amount entered to the user. When they have completed entering money, 
display the menu of available options in the vending machine (minimum 3) and their prices. The user may choose as many items as their money allows, 
and after each selection they should be allowed to end their machine usage and have their remaining money returned.
'''

# count the money
total_amount = 0
# range constrain
amount_range = range(0,6)
# ask the amount
amount = float(input('please insert the money (up to $5): '))
total_amount += amount


if amount in amount_range:
    print(f'your total amount: {amount}')
    
else:
    amount = float(input('please insert the money (up to $5): '))

    #print the menu
print('1: Soda, Price: $3')
print('2: Ice Cream, Price: $5')
print('3: Pretzels, Price: $2')

choice = int(input('please choose an item: '))

# check if we have money
while total_amount >0: 
    if choice == 1:
        total_amount -= 3
        print(f'you have left ${amount}')
        print(f'please grab your {total_amount} of change')

    elif choice == 2:
        total_amount -= 5
        print(f'you have left ${amount}')
        print(f'please grab your {total_amount} of change')
    
    elif choice == 3:
        total_amount -= 2
        print(f'you have left ${amount}')
        print(f'please grab your {total_amount} of change')

        #break if we dont have money
if total_amount == 0:
    print('you dont have any money')
    print('please insert more money to buy something else')




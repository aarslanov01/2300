# count the money
total_amount = 0
# range constraint
amount_range = range(0,6)
# ask the amount
amount = float(input('please insert the money (up to $5): '))
total_amount += amount


if amount in amount_range:
    print(f'your total amount: {amount}')
    
else:
    amount = float(input('please insert the money (up to $5): '))
   
    
    #print the menu
print('\n1: Soda, Price: $3')
print('2: Ice Cream, Price: $5')
print('3: Pretzels, Price: $2')

choice = int(input('please choose an item: '))

# check if we have money
while total_amount >0: 
    if choice == 1:
        total_amount -= 3
        print(f'\nyou have left ${total_amount}')
        print(f'please grab your {total_amount} of change')
        break

    elif choice == 2:
        total_amount -= 5
        print(f'\nyou have left ${total_amount}')
        print(f'please grab your {total_amount} of change')
        break
    
    elif choice == 3:
        total_amount -= 2
        print(f'\nyou have left ${total_amount}')
        print(f'please grab your {total_amount} of change')
        break

        #break if we dont have money
if total_amount == 0:
    print('\nyou dont have any money')
    print('please insert more money to buy something else')


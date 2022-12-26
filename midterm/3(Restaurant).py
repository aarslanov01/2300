'''
Write a program to allow a user to order food and beverage from a restaurant. The program should:

Accept the user’s name.

Assume a sales tax of 5% and a gratuity of 20%.

The user may not order less than $50, fewer than 3 items, or fewer than 2 beverages.

The program should continue until the conditions are met
'''
# who is ordering
name = input('what is your name?: ')
print(f'\nHello {name}')

#display the menu with prices upon whcih program will alcualte the total 
print('\nMenu:')
print('Food Options: pizza: $20, pasta: $40')
print('Beverages: soda: $15, vodka: $40, chai: $30')

# total order counter 
total_order = 0

# additional adjustment to the total order
sales_tax = .05
gratuity = .2

# items and beerages counter 
items = 0
beverages = 0


# loop until conditions are met 
while items < 3 or total_order < 50 or beverages < 2:
    
    order = input('what would you like to order?: ')
    
    if order == 'pizza':
        total_order += ((sales_tax * 20) + (gratuity*20) + 20) # perform the calcuations right within the loop
        items += 1
    
    
    elif order == 'pasta':
        total_order += ((sales_tax * 40) + (gratuity*40) + 40) # perform the calcuations right within the loop
        items += 1
    
    elif order == 'soda':
        total_order += ((sales_tax * 15) + (gratuity*15) + 15) # perform the calcuations right within the loop
        beverages += 1
        items += 1
        
        
    elif order == 'vodka':
        total_order += ((sales_tax * 40) + (gratuity*40) + 40) # perform the calcuations right within the loop
        beverages += 1
        items += 1
            
        
    elif order == 'chai':
        total_order += ((sales_tax * 30) + (gratuity*30) + 30) # perform the calcuations right within the loop
        beverages += 1
        items += 1

# break out when conditions are met
else:
    print('\nyou have met the minimum requirements')

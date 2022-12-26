'''
Write a program to keep track of inventory in a warehouse. 
Your program must keep track of deliveries received to update the quantity of items in the warehouse and the total cost of the inventory in 
the warehouse. Your program must accept deliveries and orders (inputs and outputs) in order to maintain a running balance. 
At any point in the program, the warehouse could be asked for its stock value. It should:

1. Accept incoming orders.

2. Accept outgoing orders.

3. Update the inventory.

4. Provide a total dollar amount of the warehouse’s inventory.
'''

# create the counter for the quantity and the total cost
qty = 0
total_cost = 0

# keep track of recieved and released items 
recieved_items = []
released_items = []

#looop unless qty and cost negative
while qty >=0 or total_cost >=0:
    process = int(input('to recieve an inventory press 1, to release press 2, to stop press 3: '))
    
    if process == 1:
        recieve = str(input('Please enter the items recieving: '))
        recieved_items.append(recieve) #append the items name 
        qty += 1 # add the item into counter
        
        recieved_price = float(input('what is the recieving price?: '))
        total_cost += recieved_price
        #output the results
        print(f'\ninventories recieved: {recieved_items}')
        print(f'total remaining price: ${total_cost}')
        print(f'total remaining quantity: {qty}')
        
    elif process == 2:
        release = str(input('Please enter the items to release: '))
        
        # we chould check if we have the item at all 
        if release not in recieved_items:
            print('We dont have that item in stock')
            continue
            
        else:
            released_items.append(release)
            recieved_items.remove(release) # we remove the inventory from existing items 
            qty -= 1
        
            released_price = float(input('what is the releasing price?: '))
            total_cost -= released_price
        
            print(f'\ninventories released: {released_items}')
            print(f'total remaining price: ${total_cost}')
            print(f'total remaining quantity: {qty}')
        
    elif process == 3:
        print(f'\ntotal quantity of iventories: {qty}')
        print(f'total cost of inventories are: ${total_cost}')
        print(f'thanks')
        break # we break if the user wants to stop
        
# we cannot run further if the qty and price goes negative from released inventories
else:
    print('your qty and price cannot be negative')
        


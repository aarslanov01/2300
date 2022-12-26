'''
Create a dictionary that keeps track of the USA’s Olympic medal count. 
Each key of the dictionary should be the type of medal (gold, silver, or bronze) 
and each key’s value should be the number of that type of medal the USA’s won. Say, 
the USA has 33 gold medals, 17 silver, and 12 bronze. Create a dictionary saved in the 
variable medals that reflects this information.


'''

medals = { 'Gold': ' ', 'Silver': ' ', 'Bronze': ' '}

# loop through the dictionary to find the medals
for key in medals:
    
    if key == 'Gold':
        
        # ask the amount of medals
        medal_count = int(input('How many Gold medals did you win?: '))
        # add the medals to the relevant key
        medals['Gold'] = medal_count
        
    elif key == 'Silver':
        medal_count = int(input('How many Silver medals did you win?: '))
        medals['Silver'] = medal_count
        
    elif key == 'Bronze':
        medal_count = int(input('How many Bronz medals did you win?: '))
        medals['Bronze'] = medal_count

# output the sum of total medals   
print(f'\nCongrats USA Team, you won {sum(medals.values())} medals')
print(f'Here is the breakdown: {medals}')

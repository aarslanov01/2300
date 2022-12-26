'''
Question 2.

Update the value for “Phelps” in the dictionary swimmers to include his medals 
from the Rio Olympics by adding 5 to the current value 
(Phelps will now have 28 total medals). Do not rewrite the dictionary. 
Assume swimmers = {'Manuel':4, 'Lochte':12, 'Adrian':7, 'Ledecky':5, 'Dirado':4, 
'Phelps':23}


'''


# our dictionary     
swimmers = {'Manuel':4, 'Lochte':12, 'Adrian':7, 
                'Ledecky':5, 'Dirado':4, 'Phelps':23}

# creaete the function to find the relevant swimmer
def update(swimmers):
    print('\nPhelps won some medals in Rio Olympics')
    print('We forgot to add 5 medals')
    
    # ask for the swimmer
    name = input('Whats the name of the swimmer?: ')
    new_medal = 5
    
    # if the name in our dictionary
    if name in swimmers:
        
        # add the medals
        swimmers[name] += new_medal
    # output the results    
    print(f'\n{name} now has the {swimmers[name]} medal')
        
update(swimmers)

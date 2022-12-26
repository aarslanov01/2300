'''
 Sing “99 Bottles of Beer on the Wall”:
99 bottles of beer on the wall, 99 bottles of beer.
Take one down, pass it around, 98 bottles of beer on the wall.
'''

# START THE TUNE IN YOUR HEAD

# how many beers on the wall?
beers = 99
print(f'{beers} beers on the wall')

# while there are still beers on the wall take one down
while beers != 0:
    beers -= 1
    print(f'{beers} beers on the wall, {beers} bottles of beer. Take one down, pass it around ')
    
    if beers == 0:
        print(f'{beers} on the wall')

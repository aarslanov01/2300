import random
def single_flip():
    
    heads = 0
    tails = 0
    number = ''


    while type(number) != int:
        number = int(input("how many times do you want to flip? "))

        if type(number) != int:
            print('please enter an integer')

    if type(number) == int:
        
        for n in range(0,int(number)):
            flip = random.randint(0,1)

            if flip == 0:
                heads += 1
            else:
                tails += 1
        print(f'\nThe count of heads: {heads}')
        print(f'\nThe count of tails: {tails}')
        
            
        
        
    else:
        print('flipping has been terminated')
        
def gameon_choice():
    
    choice = ''
    
    while choice not in ['y','n']:
        
        choice = input("Want to Flip again? (y or n): ")
        
        if choice not in ['y','n']:
            print('Wrong input please choose y or n ')
            
    if choice == 'y':
        return True
    else:
        return False
      
game_on = True

while game_on:
    single_flip()
    game_on = gameon_choice()
    
print('\nThanks for flipping')


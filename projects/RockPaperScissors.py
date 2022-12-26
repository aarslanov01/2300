'''
1. Use the random module to construct a game of Rock, Paper, Scissors. First the player will make a move and then the computer will make one. 
You can use the abbreviations R, P, and S instead of typing out the whole word if you'd like. Keep track of the score and play until five wins are scored.
'''

#import the library 
import random

def player(player_move):
    print(f'Your move is: {player_move}')
    
def machine(machine_move):
    print(f'Machine move is: {machine_move}')
#run evertyhing trhough main    
def main():
    #define the menu
    print('WELCOME ')
    print('☆*:.｡.o(≧▽≦)o.｡.:*☆')
    print()
    print('R for ROCK')
    print('P for PAPER')
    print('S for SCISSORS')
    print('--------------------')
    #define the rules
    print('Rules of the Game: ')
    print('> Rock beats Scissors <')
    print('> Scissors beats Paper <') 
    print('> Paper beats Rock <')
    print('--------------------')
    #list the selection
    selection = ['R','P','S']
    #counter for each player
    user_wins = 0
    machine_wins = 0
    
    #execute until conditions arent met
    while user_wins < 5 and machine_wins < 5:
        player_move = input('\nWhat is your move? (R,P,S)').upper()
        player(player_move)
        machine_move = random.choice(selection)
        machine(machine_move)
        #define the tie
        if player_move == machine_move:
            print('its a tie')
        #enforce the rules through conditional statements   
        elif player_move == 'R':
            if machine_move == 'S':
                user_wins += 1
                print('You win!')
                print('٩(◕‿◕｡)۶')
            else: 
                machine_wins +=1
                print('Computer wins')
                print('¯\_(ツ)_/¯')
                
        elif player_move == 'S':
            if machine_move == 'P':
                user_wins += 1
                print('You win!')
                print('٩(◕‿◕｡)۶')
            else: 
                machine_wins +=1
                print('Computer wins')
                print('¯\_(ツ)_/¯')
        elif player_move == 'P':
            if machine_move == 'R':
                user_wins += 1
                print('You win!')
                print('٩(◕‿◕｡)۶')
            else: 
                machine_wins +=1
                print('Computer wins')
                print('¯\_(ツ)_/¯')
    if user_wins> machine_wins:
        print()
        print('(　・ω・)⊃-[二二]')
        print('You won the game! You deserve a drink! ')
        print()
        print('｡･:*:･ﾟ’★,｡･:*:･ﾟ’☆｡･:*:･ﾟ’★,｡･:*:･ﾟ’☆')
        print('｡･:*:･ﾟ’★,｡･:*:･ﾟ’☆｡･:*:･ﾟ’★,｡･:*:･ﾟ’☆')
        print('｡･:*:･ﾟ’★,｡･:*:･ﾟ’☆｡･:*:･ﾟ’★,｡･:*:･ﾟ’☆')
        print('｡･:*:･ﾟ’★,｡･:*:･ﾟ’☆｡･:*:･ﾟ’★,｡･:*:･ﾟ’☆')
            
    else:
        print()
        print('.･ﾟﾟ･(／ω＼)･ﾟﾟ･.')
        print('you lost the game man!')

        
    
main()  
    

'''
Build an ATM Machine
'''

# greet our customers 
print('*** WELCOME ***')
print('(づ ◕‿◕ )づ')

initial_balance = 0

#start couning the initial balance
starting_balance = float(input('What is your starting balance?: '))

initial_balance += starting_balance

print(f'\nYour balance is: ${initial_balance}')

# function to depoit the money 
def amountDeposit(initial_balance, deposit_amount):
    initial_balance += deposit_amount
    print(f'\nYour new balance is: ${initial_balance} ')
    return initial_balance

# function to withdraw the money 
def amountWithdraw(initial_balance, withdrawal_amount):
    if withdrawal_amount > initial_balance:
        print('\nYou cannot withdraw more than your balance')
        print("┐('～`;)┌")
        
    else:
        initial_balance -= withdrawal_amount
        print(f'\nYour new balance is: ${initial_balance} ')
        return initial_balance
        
def main():
    # taking the transaction input
    transaction = input('to deposit, enter: d, to withdraw, enter: w, to quit, enter: q')
    
    # keep asking the deposit or withdrawal until we quit
    while transaction == 'd' or transaction == 'w':
        
        if transaction == 'd':
            deposit_amount = 0
            amount = float(input('\nHow much do you want to deposit? '))
            deposit_amount += amount
            amountDeposit(initial_balance, deposit_amount)
            transaction = input('\nto deposit, enter: d, to withdraw, enter: w, to quit, enter: q')
            
        elif transaction == 'w':
            withdrawal_amount = 0 
            amount = float(input('\nHow much do you want to withdraw? '))
            withdrawal_amount += amount
            amountWithdraw(initial_balance, withdrawal_amount)
            transaction = input('\nto deposit, enter: d, to withdraw, enter: w, to quit, enter: q')
    
    # we quit 
    if transaction == 'q':
        print(f'\nYour balance is: {initial_balance}')
        print('Thank you for using the ATM')
        print('*** ENJOY YOUR DAY ***')
        print('ヽ(♡‿♡)ノ')
    
main()

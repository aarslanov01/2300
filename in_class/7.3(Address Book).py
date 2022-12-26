'''
Name and Email Addresses: Write a program using various functions that keeps names and email 
addresses in a dictionary as key-value pairs. The program should display a menu 
[write a function displayMenu] that lets the user choose from following options:

> look up and return a person’s email address if it exists [write a function lookupEmail],
> add a new name and email address and return the updated dictionary [write a function addEmail],
> change an existing email address and return the updated dictionary [write a function updateEmail] and
> delete an existing name and email address and return the updated dictionary [write a function deleteEmail].


'''


# create the menu
def displayMenu():
    print()
    print('Enter: [ look ]   to look up an email')
    print('Enter: [ add ]  to add new email address')
    print('Enter: [ update ] to change an existing email')
    print('Enter: [ delete ] to delete an existing email')
    print('Enter: [ quit ]   to quit the program')
    
    # take the choice convert it into lower just in case
    choice = input('Please choose: ').lower()
    
    return choice

# looking up emails
def lookupEmail(emails):
    name = input('Input the name: ')
    
    #output the key and value 
    print(emails.get(name))

# adding emails     
def addEmail(emails):
    # the name we want to add
    name = input('Input the name: ')
    
    # email we want to add
    email = input('Input the email: ')

    emails[name] = email
           
    print(f'You added {name} with email: {email}')
           
def updateEmail(emails):
    name = input('Input the name: ')
           
    if name in emails:
        email = input('What is the new email?: ')
           
        emails[name] = email
           
    else:
        print('I didnt find the name')
           
def deleteEmail(emails):
    name = input('Input the name: ')
           
    if name in emails:
        del emails[name]
           
    else:
        print('I didnt find the name')
           
def main():

    emails = {}
    
    choice = []

    # run the menu until we quit       
    while choice != 'quit':
        choice = displayMenu()
        
        if choice == 'look':
            lookupEmail(emails)
           
        elif choice == 'add':
            addEmail(emails)
           
        elif choice == 'update':
            updateEmail(emails)
           
        elif choice == 'delete':
            deleteEmail(emails)
    print()        
    print(emails)
              
main()

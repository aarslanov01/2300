'''
rite a function getStrFeatures(userInput) that takes userInput as a parameter, 
then counts and returns how many uppercase, lowercase, numbers, and spaces are
contained in a given string. Be sure to call this function from main and print out 
the results returned.

'''

def getStrFeatures(userInput):
    # create a placeholders for each sceanrio
    lower_case = []
    upper_case = []
    numbers = []
    spaces = []
    
    # iterate throught the input to match the criteria
    for letter in userInput:
        if letter.islower():
            lower_case.append(letter)
            
        if letter.isupper():
            upper_case.append(letter)
            
        if letter.isdigit():
            numbers.append(letter)
            
        if letter.isspace():
            spaces.append(letter)
            
    # print out the number of each scenario using the len()          
    print(f'the number of lower cases are: {len(lower_case)}')
    print(f'the number of upper cases are: {len(upper_case)}')
    print(f'the number of digits are: {len(numbers)}')
    print(f'the number of spaces are: {len(spaces)}')

def main():
    
    userInput = input('please input a string: ')
    getStrFeatures(userInput)

main()

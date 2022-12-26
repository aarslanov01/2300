
'''
Question:

Create a "main" function.
● This function should:
○ Prompt the user for three numbers, one at a time
○ Prompt the user, after each entry, for the mathematical operator. You must
include addition, subtraction, multiplication, and division.
NOTE: The prompts must be exactly as shown in the "Sample output" section.
○ Print the operations provided in the inputs.
● NOTE: The output must be exactly as shown in the "Sample output" section, with
variance in the operators used.
● This program will loop in asking the user for inputs and operators until the user
enters the “=” operator. It will then exit the program

'''

# run thru main
def main():
    
    print()
    print('For addition: + ')
    print('For substraciton: - ')
    print('For multiplication: * ')
    print('For division: / ')
    print('to end and see the results: = ')
    print()
    
    # set the counters for both variables 
    choice = ''
    result = 0
    
    # set the ligical constrain
    while choice != '=':
        # ask for the numbers and choices
        num1 = int(input('Input first number: '))
        choice = input('Choose the operations (+,-,*,/): ')
        num2 = int(input('Input second number: '))
        
        #check against the operation
        if choice == '+':
            result = num1 + num2
            
        elif choice == '-':
            result = num1 - num2
            
        elif choice == '*':
            result = num1 * num2
            
        elif choice == '/':
            result = num1 / num2
        # printout the results    
        print(f'Your result is: {result}')
            
        choice = input('Choose your last operation (+,-,*,/): ')
             
        num3 = int(input('Input third number:'))
        
        if choice == '+':
            result += num3
            
        elif choice == '-':
            result -= num3
            
        elif choice == '*':
            result *= num3
            
        elif choice == '/':
            result = result/num3
            
        print(f'Your result is: {result}')
            
        print('end you program by: =')
        
        choice = input('Choose your last operation (+,-,*,/,=): ')
        
        if choice == '=':
            print(f'Your result is: {result}')
            
# end teh function 
main()   



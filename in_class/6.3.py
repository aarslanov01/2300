'''
Write a function addUpDigits(digitString) that takes digitString as parameter 
(a series of single-digit numbers with nothing separating them.) The function should return
the sum of all the single digit numbers in the string. For example, if the user enters 2514,
the method should return 12, which is the sum of 2, 5, 1, and 4. Be sure to call this function
from main and print out the results returned

'''

def addUpDigits(digitString):
    
    # turn the input into the string
    string = str(digitString)
    total = 0
    
    for n in string:
        total +=  int(n) # - string into integer
        
    return total 
        
def main():
    
    digitString = input('input the the string of digits: ')
    print(addUpDigits(digitString))
    
main()
        

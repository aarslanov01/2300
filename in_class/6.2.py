'''
Write a function mostFreqCh(userInput) that takes userInput as a parameter, 
and returns the character that appears most frequently in the string along with the number 
of times this character appeared. Be sure to call this function from main and print out the results returned.


'''

def mostFreqCh(userInput):
    # string to compare the characters against
    copy_string = str(userInput)
    most_common = []
    frequency = 0
    
    for l in copy_string:
        #set a counter within the copyied string 
        count = 0
        for char in userInput:
            # compare the input characters to the characters in copy string 
            # if we identify similarities
            if char == l:
                # count it 
                count += 1
                
        #check the count against the total frequency of the character
        if count == frequency:
            frequency = count
            # append the character
            most_common.append(l)
        
        # if the count of the similar character is more than given total frequency of characters
        elif count > frequency:
            # reassign the value
            frequency = count
            # get rid of previous string
            most_common.clear()
            # create new
            most_common.append(l)
            
            print(f'most frequent is {most_common}')
            print(f'it appeared {frequency} times')
            

def main():
    
    userInput = input('Input the string: ')
    mostFreqCh(userInput)
    
    
main()


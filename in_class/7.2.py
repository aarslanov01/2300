'''
Write a function countLetter that takes a word as a parameter and returns a dictionary 
that tells us how many times each letter appears in the word (no need to account for absent letters). 
Develop your logic using dictionaries only. Save the count result as a dictionary. Display your output 
in the main() function.

'''

# create the empty dictiory for letters
letters = {}

# funciton to count the letters
def countLetter(letters):
    word = input('input the word: ').lower()
    print(f'The given word is: {word}')
    
    # create a copy string to check against
    copy_word = str(word)
    
    # loop through the letters
    for n in word:
        # create a counter while looping to count the letters
        count = 0
        for u in copy_word:
            # compare the letters in original input to the against the copy
            if n == u:
                count += 1
                
                #create a dictionary for each looped letter
                letters[u] = count
                

def main():
    countLetter(letters)
    print('\nThe count of the words as follows: ')
    print(letters)
    

main()

'''
Write a program with a function that accepts a string as 
an argument and returns the number of vowels that the string 
contains. The application should have another function that 
accepts a string as an argument and returns the number of 
consonants that the string contains. The application should 
let the user enter a string and should display the number of 
vowels and the number of consonants it contains.

'''


# take an input for the string 
my_string = input('please enter a string: ')

def vowel(my_string):
    #vowels in english alphabet
    vowels = ['a', 'e', 'i', 'o' , 'u']
    # placeholder for vowels
    num_vowels = []
    for n in my_string.lower():
            if n in vowels: #<-- see if the letter in the string is in vowels
                num_vowels.append(n)
    print(f"the number of vowels are: {len(num_vowels)}") #<-- output the length of the vowels
                
def consonant(my_string):
    #consonants in english alphabet
    consonants = ['b', 'c', 'c', 'f', 'g', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 's', 't', 'v', 'x', 'z','h','w','r']
    #placeholder for consonants
    num_consonants = []
    for n in my_string.lower():
            if n in consonants: #<-- see if the letter in the string is in consonants
                num_consonants.append(n)
    print(f"the number of consonants are: {len(num_consonants)}") 

# call in both functions 
vowel(my_string)
consonant(my_string)

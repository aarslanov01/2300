'''
Question 1.

Concatenate the followiing dictionaries to create a new one

'''
d1={1:10, 2:20} 
d2={3:30, 4:40} 
d3={5:50, 6:60}

# create a placeholder for the new dictionary
d4 = {}

# define the function
def dict_concat(d1,d2,d3):
    #use for loop to loop through each key
    for d in(d1,d2,d3):
        #append into new dictionary using update
        d4.update(d)
    return d4
    
#run using main
def main():
    dict_concat(d1,d2,d3)
    print()
    print(d4)
    
main()    

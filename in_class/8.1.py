'''
Question 2.

Concatenate the following dictionaries to create a new one. 
If a key repeats across the three dictionaries, you have to add the values corresponding to the key.

'''

d1={1:10, 2:20} 
d2={1:20, 3:30, 4:40} 
d3={5:50,6:60,3:60}

d4={}

#create a function
def concatenate_d(d1,d2,d3):
    
    # loop through each key and value in the given dictionaries
    for d in (d1,d2,d3):
        # loop to compare the keys
        for k in d:
            # add the keys if they are in d4
            if k in d4:
                d4[k] = d4[k] + d[k]
            # assign the new if they arent    
            else:
                d4[k] = d[k]
    return d4
# run trhough the main function        
def main():
    concatenate_d(d1,d2,d3)
    print()
    print(d4)
    
main()    

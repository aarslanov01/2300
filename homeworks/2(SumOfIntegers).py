'''
Question 1: Sum of integers

Write a function, add_it_up(), that takes a single integer as input and returns the sum of 
the integers from zero to the input parameter.
The function should return 0 if a non-integer is passed in.

'''
# define the function 
def add_it_up(number):
    # set the counter
    counter = 0
    #go through the range
    for n in range(0,number):
        counter += n
        print(counter)
# return through main
def main():
    number = int(input('input an integer: '))
    add_it_up(number)
    
main()

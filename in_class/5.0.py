#take the inputs
def addItems2List():
    process = 1
    my_list = []
    while process == 1:
        num = int(input("Enter an integer: "))
        my_list.append(num)
        choice = input("Add another? y/n")
        if choice == 'n':
            process -= 1
        
    
    return my_list

def distribList(my_list):

# find lowest, highest, total and average
    low = min(my_list)
    high = max(my_list)
    
    total =  sum(my_list)
    
    average = total/len(my_list)

# display the results
    print(f'\nthe lowest value is: {low}')
    print(f'the highest value is: {high}')
    print(f'the total value is: {total}')
    print(f'the average value is: {average}')
    
# define the main     
def main():
    the_list = addItems2List()
    
    print(the_list)
    print(distribList(the_list))
main()

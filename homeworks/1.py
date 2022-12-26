'''
Problem:
In this Madlibs-style exercise, use [lists] and the [random module] to create startup ideas of the form: 
My startup is _ for _! First, [ write a list of company names ] and then [ write a second list of animals ]. 
Randomly choose from each list to construct something like "My startup is Uber for koalas!"

'''
#import the random library 
import random

companies = ['Abatz', 'Kaymbo', 'Oozz', 'Demimbu', 'Jaxnation', 'Quatz', 'Dabfeed', 'Jabberbean', 'Twinte']
animals = ['Brindled gnuCat', 'long-tailed Gorilla', 'western lowland Blue wildebeest Alpaca', 'elegant crested Snake', 
           'buttermilk Western patch-nosed snake Rat', 'desert kangaroo']
# start the program 
choice = input('To start your program enter: start').lower()
#execute until input to stop
while choice != 'stop':
    #use random.choice to select random object from the list
    print(f'\nMy startup name is {random.choice(companies)} for {random.choice(animals)}!')
    choice = input('to run again input: "run" to stop: "stop"')
    
    if choice == 'run':
        continue
    else:
        choice = input('to run again input: "run"; to stop: "stop"')
    

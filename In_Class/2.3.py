'''
Write a program that asks the user to enter a person's age. The program should display a message indicating whether the person is an infant, a child, a teenager, an 
adult, or a senior citizen. Following are the guidelines:
If the person is 1 year old or less, he or she is an infant.
If the person is older than 1 year, but younger than 13 years, he or she is a child.
If the person is at least 13 years old, but less than 20 years old, he or she is a teenager.
If the person is at least 20 years old, but less than 65 years old, he or she is an adult.
Otherwise the person is a senior citizen!
'''


# ask the age with an integers
age = int(input("enter your age: "))

# create the logic
if age <= 1:
    print('you are a infant')
    
elif age > 1 and age < 13:
    print('you are a child')
    
elif age >= 13 and age < 20:
    print('you are  a teenager')
    
elif age >= 20 and age < 65:
        print('you are an adult')
        
else: 
    print('you are a senior citizen')

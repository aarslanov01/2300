'''
A person is eligible to be a US Senator who is at least 30 years old and has been a US citizen for at least 9 years. 
A person is eligible to be a US Representative who is at least 25 years old and has been a US citizen for at least 7 years. 
Write a program requesting a user to enter their age and length of citizenship 
to determine whether they are eligible to run for the House, the Senate, or both. Print out the messages to the user accordingly.
'''
# determine the age and the citizenship
age = int(input("Age? "))
citizenship = int(input("Length of citizenship? "))

# build the comparison opereators to match the criteria
if age >= 25 and citizenship >= 7:
    print("You can be a rep")
if age >= 30 and citizenship >= 9:
    print("You can be a senator")

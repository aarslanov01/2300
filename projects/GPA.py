# for the convenience we sum prebuisness_gpa(line 37) with overall gpa (line 44)
# to create a threshold for approval 
gpa_threshold = 4.5

# usual credits (3) times reuired amount of classes (8) to calculate line 43
credit_hours = 3*8

# we create a binomial counter to apporve the comunication requirement 
#if 1 and reject if 0
req_counter = 0


com1010 = str(input('Have you completed COM 1010? (y/n): ')).lower()
eng2150 = str(input('Have you completed ENG 2150? (y/n): ')).lower()

# we create the comparison
if com1010 == 'y' and eng2150 == 'y':
    #if both constraints are satisfied we add 1 to the counter
    req_counter += 1
    print('Nice job, you have satisfied communication requirements!')
elif com1010 != 'y' or eng2150 != 'y':
    #else we add 0
    req_counter += 0
    print('Sorry, you are not satisfied communication requirements :(')
    
# display the grades
print('\nUse the following table to enter your numeric grades for each of the pre-business courses:')
print('\nA = 4.0,  A- = 3.7')
print('B+ = 3.3, B = 3.0  B- = 2.7')
print('C+ = 2.3, C = 2.0  C- = 1.7')
print('D+ = 1.3, D = 1.0')
print('F = 0.0')
print('\n')

acc2101 = float(input('Your grade in ACC 2101: '))
cis2200 = float(input('Your grade in CIS 2200: '))
eco1001 = float(input('Your grade in ECO 1001: '))
eco1002 = float(input('Your grade in ECO 1002: '))
eng2100 = float(input('Your grade in ENG 2100: '))
law1100 = float(input('Your grade in LAW 1101: '))
calc = float(input('Your grade on one of the calculus: '))
sta2000 = float(input('Your grade in STA 2000: '))

# calculating the pre business gpa using formula 
prebusiness_gpa = ((acc2101*3)+(cis2200*3)+(eco1001*3)+(eco1002*3)+(eng2100*3)+(law1100*3)+(calc*3)+(sta2000*3))/credit_hours

print(f'Holy Moly Ravioli! Your pre-business Gpa is: {prebusiness_gpa}')



credits_completed = int(input('How many credits completed?: '))
overall_gpa = float(input('What is your overall Baruch GPA?: '))

# sum the gpa and compare it with a threshold in line 4
gpa = (prebusiness_gpa+overall_gpa)

# build the logic
if gpa > gpa_threshold and req_counter == 1 and credits_completed >= 45:
    print('You are eligible for Zicklin! Congrats!')
elif gpa < gpa_threshold and req_counter == 0 and credits_completed < 45:
    print('You suck!')

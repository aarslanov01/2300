'''
An old woodchuck can chuck 1 log per minute per year of age (4 or 5 years old)

A young woodchuck can chuck 2 logs per minute per year of age (0.5 years up to 2 years)

A middle-aged woodchuck will chuck 1.5 logs per minute per year of age. (2 years up to 4 years)



We need a representative sample of woodchucks to properly calculate this answer, so please create 5 woodchucks of varying ages 
(0.5 years through 5 years old) via user input and calculate how many logs they can chuck on average within 15 minutes.
'''

# preformance measurement
old = 1

young = 2

middle_age = 1.5

time = 15

# total time counter
total_time = 0

# woodchucks counter
woodchucks = 0

# loop until we hit 5
while woodchucks != 5:
    woodchuck = float(input('how old is your woodchuck: '))
    
    if woodchuck == 4 or woodchuck == 5:
        total_time += old*time
        woodchucks += 1
        
    elif woodchuck > 0.5 and woodchuck <= 2:
        total_time += young*time
        woodchucks += 1
        
    elif woodchuck >= 2 and woodchuck <= 4:
        total_time += middle_age*time
        woodchucks += 1

# break out when we hit 5        
if woodchucks == 5:
    print(f'average = {total_time/5}')


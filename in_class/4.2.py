'''
Present Investment Amount
'''
# fv i.e. future expected earnings
# r i.e. expected annual interest rate
# n i.e. timeframe
fv = float(input('What is the Amount of Future Expected Earnings?: '))
r = float(input('What is Expected Annual Interest Rate? (%): '))
n = float(input('What is the Timeframe? (years): '))

# convert the percentages 
r_converted = r/100

# pv i.e. present value
pv = fv * (1/((1+r_converted)**n))

print(f"\nDear user, you have to invest: ${pv}")
print(f"In order to have ${fv} in {n} years with an \ninterest rate of {r}%")

'''
Write a program to take an input number (account for both ints and floats) and return the circumference of a circle 
with the number as a radius. (Hint: Don't worry about the pythonic way of using the math lib for pi; use the static float 3.14159).
'''

pi = 3.14
radius = float(input('please enter your radius (only int or float): '))

# assign the formula to the variable
circumference = 2*pi* radius

# return the result

print(f"The circumference is: {circumference}")

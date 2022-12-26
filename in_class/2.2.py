'''
Write a program statement that displays 'Speed is normal' if the speed variable is within the range of 24 to 56. If the speed variable's value is outside this range, display 'Speed is abnormal'.
'''


# we set the input to an integer for the convenience of matheatical comparison
speed = int(input("whats the speed?: "))

# create the logic
if speed > 23 and speed < 57:
    print('your speed is normal')
else: 
    print('your speed is abnormal')

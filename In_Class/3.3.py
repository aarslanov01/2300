'''
Write a while loop that lets the user enter an integer between 1 and 10. The number should be multiplied by 7 and 
subtracted by a second integer that the user also enters in any range. 
The result should be assigned to a variable named prodNum. The loop should keep iterating as long as prodNum is less than 100. Print prodNum
'''


number = int(input('please enter an integer in the range 1 - 10: ')) 
number2 = int(input('please enter second number in any range'))
check_range = range(1,11)
prodNum = 0

while number not in check_range and prodNum < 100:
        number = int(input('please input the integer in the range 1 - 10: '))
    
        while number in check_range:
        mult_num = number * 7
        prodNum += mult_num
        print(prodNum)
    
    
        second_integer = int(input('what is the second integer? '))
        prodNum -= second_integer
        print(prodNum)
else:
    print(prodNum)
    break

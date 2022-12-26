'''
Question 3: Rectangle

Write a Python class named [Rectangle] constructed by a [length and width] and a method which will 
[compute the area of a rectangle]

'''
# define the class
class Rectangle:
    
    
    def __init__(self, length, width):
        self.length = length
        self.width = width 

    #define the calculation     
    def calculate_area(self):
        print(f'\nThe area is: {self.length * self.width}')
       
        
def main():
    #take the inputs for width and length
    width = int(input('input the width: '))
    length = int(input('input the length: '))
    rectangle_area = Rectangle(width, length)
    rectangle_area.calculate_area()
    
if __name__ == "__main__":
    main()

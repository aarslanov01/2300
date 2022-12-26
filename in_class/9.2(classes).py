'''
Question 3.
Tesla Taxi

'''
class TeslaTaxi(Tesla):
    def __init__(self, model, color,number, address):
        # inherit the properties from tesla and add relevant properties for taxi
        super().__init__ (model, color)
        self.model = model
        self.color = color
        self.number =  number
        self.meter = 0
        self.flat_charge = 5
        self.variable_cost = 2.50 #per mile
        self.address = address
    # calaculate the costs for the ride
    def cost_calculator(self, miles):
        self.meter += (self.flat_charge + (self.variable_cost * miles))
        print(f'You will be picked up by {self.color} Tesla {self.model}')
        print(f'Look for plate #: {self.number}')
        print(f'Your address is: {self.address}')
        print(f'You will owe {self.meter}')
        
        
# run through main with taking relevant inputs
def main():
    print('Welcome to Tesla Taxi')
    print('Please input the following information: ')
    my_taxi = TeslaTaxi(input('What model is it?: '), input('What color is it?: '),input('Whats the number?: '), input('Where we going today boss? '))
    my_taxi.cost_calculator(int(input('How many miles is it? ')))
    my_taxi.result()
                       
    
if __name__ == '__main__':
    main() 
    
    

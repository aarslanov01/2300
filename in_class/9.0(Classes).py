'''
Question 1.
Make me a truck.

'''


class Truck():
    # define the properties of a truck
    def __init__(self, brand, model, max_load, type):
        self.brand = brand
        self.model = model
        self.type = type
        self.max_load = 3325
        self.current_load = 0
        self.gas_tank = 23
        self.fuel_level = 0
        self.mpg = 24

    def gaz(self, drive):
        return self.gas_tank - drive/self.mpg 
    
    def fuel_up(self):
        self.fuel_level = self.gas_tank
        print('Gas tank is full.')
        
    def destination(self, city):
        self.destination.append(city)
        print(f'you are heading to {self.destination}')
    # load the truck
    def load_up(self,load):
        self.current_load += load
        # if load more than maximum display the warning
        if self.current_load >= self.max_load:
            print('the load exceeds the limits')
            
        else:
            print(f'you have loaded {self.current_load}')
            print(f'{self.model} has remaining {self.max_load - self.current_load}')
    # unload the truck 
    def unload(self, load):
        self.current_load -= load
        # if unoading mass larger than current weight display teh warning
        if load > self.current_load:
            print(f'{self.model} has less weight than you requesting ')
            
        else:  
            print(f'{self.model} has weight of {self.current_load}')
# run the program through main            
def main():
    myTruck = Truck('Ford','F1-50','6 Door', 3325)
    myTruck.fuel_up()
    myTruck.load_up(int(input('what is the load? ')))
    myTruck.unload(int(input('how much would you like to unload?: ')))
    
if __name__ == '__main__':
    main()

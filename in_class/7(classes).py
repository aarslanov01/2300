'''
Question 2.
Tesla
'''

class Tesla():
    # define the attribute of Tesla
    def __init__(self, model, design):
        self.model = model
        self.design = design
        self.charged = 0
        self.charge_max = 104
        self.kWpm = 0.27
        
        
    #charge the battery 
    def charge(self):
        self.charged = self.charge_max
        print(f'{self.model} battery is full')
    # define the usage     
    def charge_usage(self, miles):
        return self.charge_max - miles/self.kWpm
        
    # input the usage and mileage together    
    def drive(self, mileage):
        print(f'{self.model} is driving')
        self.charge_update(self.charge_usage(mileage))
        print(f'you have {self.charged} watts remaining')
        
        
    # define the chargin update   
    def charge_update(self, new_charge):
        if new_charge <= self.charge_max:
            new_charge = self.charged
            
        else:
            print('you charged too much')
            
    
    
# run the program through main by taking the relevant inputs
def main():
    my_tesla = Tesla(input('What model is it?: '), input('What color is it?: '))
    my_tesla.charge()
    my_tesla.drive(int(input('how many miles?: ')))

if __name__ == '__main__':
    main()

class Employee():
    '''a class for employee'''
    def __init__(self, f_name, l_name, salary):
        self.f_name = f_name
        self.l_name = l_name
        self.salary = salary
    
    def give_rise(self, num = 5000):
        '''a function to increase salary'''
        self.salary += num
        return self.salary
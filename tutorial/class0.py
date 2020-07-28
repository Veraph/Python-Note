# class.py -- first attempt to use Class
class Restaurant():
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        '''describe the property of the restaurant'''
        print("The name of the restaurant is", self.restaurant_name)
        print("The cuisine type is", self.cuisine_type)
    
    def open_restaurant(self):
        '''Show the restaurant is running'''
        print("The restaurant", self.restaurant_name, "is opening")
    
    def set_number_served(self, num):
        '''set the number of people can be served'''
        self.number_served = num
    def increment_number_served(self, nums):
        '''increase the number of people be served'''
        self.number_served += nums

# create sub class
class ChineseRestaurant(Restaurant):
    def __init__(self, restaurant_name, cuisine_type):
        '''initialize property of super class'''
        super().__init__(restaurant_name, cuisine_type)
        self.panda_nums = 1

# create sub class
class IceCreamStand(Restaurant):
    def __init__(self, restaurant_name, cuisine_type):
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = ['lemon', 'apple', 'banana']

    def show_flavors(self):
        print("We have: ")
        for flavor in self.flavors:
            print(flavor)
        print("flavors!")

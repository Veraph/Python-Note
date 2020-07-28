import unittest
from employ import Employee

class TestEmployee(unittest.TestCase):
    '''test for Employee class'''
    def setUp(self):
        '''create an instance'''
        f_name = 'Mengwei'
        l_name = 'Jiang'
        salary = 300000
        self.my_employee = Employee(f_name, l_name, salary)

    def test_default_raise(self):
        '''test for default raise'''
        raised_salary = self.my_employee.give_rise()
        self.assertEqual(raised_salary, 305000)
    
    def test_custom_raise(self):
        '''test for custom raise'''
        raised_salary = self.my_employee.give_rise(300000)
        self.assertEqual(raised_salary, 600000)

unittest.main()
import unittest
from employee import Employee

class TestEmployeeRaise(unittest.TestCase):
    """Test for Employee class"""
    
    def setUp(self):
        """Create an employee and test raise functionality for custom and default"""
        self.employee = Employee('John', 'Rutherford', 50_000)

    def test_give_default_raise(self):
        self.employee.give_raise()
        self.assertEquals(self.employee.salary, 55_000)

    def test_give_custom_raise(self):
        self.employee.give_raise(10_000)
        self.assertEquals(self.employee.salary, 60_000)

if __name__ == '__main__':
    unittest.main()
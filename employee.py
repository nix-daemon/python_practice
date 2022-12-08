class Employee:
    """A simple attempt to model an employee"""
    def __init__(self, first, last, salary):
        self.first = first
        self.last = last
        self.salary = salary 

    def give_raise(self, raise_ = 5000):
        self.salary = self.salary + raise_
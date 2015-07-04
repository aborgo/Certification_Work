"""
Basic class and OOP programming, creates the coconut object
and the aiblity to inventory them.
"""

class Coconut:
    def __init__(self, name, weight):
        self.name = name
        self.weight = weight

class Inventory:
    def __init__(self):
        self.nut = []
    def add_coconut(self,coconut):
        if isinstance(coconut,str):
            raise AttributeError
        else:
            self.nut.append(coconut)
    def total_weight(self):
        tw = 0
        for coconut in self.nut:
            tw += coconut.weight
        return tw

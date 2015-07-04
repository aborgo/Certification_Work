import unittest
from coconuts import Inventory, Coconut

class testing_coconuts(unittest.TestCase):
    
    def test_coconut_weight(self):
        sa = Coconut('south_asian', 3)
        me = Coconut('middle_eastern', 2.5)
        am = Coconut('american', 3.5)
        self.assertNotEqual(sa.weight,me.weight)
        self.assertNotEqual(sa.weight,am.weight)
        self.assertNotEqual(me.weight,am.weight)
    
    def test_add(self):
        inv = Inventory()
        sa = Coconut('south_asian', 3)
        me = Coconut('middle_eastern', 2.5)
        am = Coconut('american', 3.5)
        clist = [sa,sa,me,am,am,am]
        for i in clist:
            inv.add_coconut(i)
        expected = 19.0
        observed = inv.total_weight()
        self.assertEqual(observed, expected)
        
    def test_string_error(self):
        inv = Inventory()
        self.assertRaises(AttributeError, inv.add_coconut, 'american')

if __name__ == '__main__':
    unittest.main()

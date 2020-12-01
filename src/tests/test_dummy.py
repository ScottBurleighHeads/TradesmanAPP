from main import add
import unittest
class Test_dummy(unittest.TestCase):
    
    def test_add(self):
        self.assertEqual(add(2,3),5)

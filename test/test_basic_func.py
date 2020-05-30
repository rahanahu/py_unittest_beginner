import unittest
import sys
import os

TO_ROOT = '../'
HERE = os.path.dirname(__file__)
sys.path.append(os.path.join(HERE, TO_ROOT))
from source.basic_func import *

class TestBasicFunc(unittest.TestCase):
    def test_add_num(self):
        self.assertEqual(add_num(2,3),5)
        pass
    
    def test_sum_list(self):
        self.assertEqual(sum_list([1,2,3,4,5]), 1+2+3+4+5)

if __name__ == "__main__":

    pass
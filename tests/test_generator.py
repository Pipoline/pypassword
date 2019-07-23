import unittest
from pypassword.pypassword import generate


class GenerateSimplePasswordCase(unittest.TestCase):
    password = generate()
    
    
class test_special_password:
    password = generate(special=True)
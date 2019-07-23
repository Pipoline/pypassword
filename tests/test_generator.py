import unittest
from pypassword.pypassword import generate


class GenerateSimplePasswordCase(unittest.TestCase):
    password = generate()


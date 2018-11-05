import unittest
from pypassword.pypassword import password_generator


class GenerateSimplePasswordCase(unittest.TestCase):
    password = password_generator()


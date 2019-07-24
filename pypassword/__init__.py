"""
Pypassword Library
~~~~~~~~~~~~~~~~~~~~~
Pypassword is password generating library, written in Python, for human beings.

Basic usage:
>>> import pypassword
>>> pypassword.generate()
'uVRf4TE7YLVd'

or
Generate password with length 20 chars
>>> pypassword.generate(20)
'4QkD741kvSXoMAQo616l'
"""

from .pypassword import generate

__all__ = ['generate']

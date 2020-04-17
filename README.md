# random-password

This is a simple password generator written in python.

[![Build Status](https://travis-ci.org/Pipoline/pypassword.svg?branch=master)](https://travis-ci.org/Pipoline/pypassword)
[![Docker pulls](https://img.shields.io/docker/pulls/pipoline/pypassword.svg)](https://hub.docker.com/r/pipoline/pypassword)
![Codecov](https://img.shields.io/codecov/c/github/pipoline/pypassword)  
![PyPI - Downloads](https://img.shields.io/pypi/dm/pypassword)  
If you want to buy me some coffee :D [![ko-fi](https://www.ko-fi.com/img/donate_sm.png)](https://ko-fi.com/G2G8LB08)


## Usage

### Basic python usage:

```
>>> import pypassword
>>> pypassword.generate()
'uVRf4TE7YLVd'
```

or

Generate password with length 20 chars

```
>>> pypassword.generate(20)
'4QkD741kvSXoMAQo616l'
```

### Basic cli usage:
```
usage: pypassword.py [-h] [-s SIZE] [-x]

optional arguments:
  -h, --help            show this help message and exit
  -s SIZE, --size SIZE  Random string size
  -x                    When set, use special characters
```
 
### Basic docker usage: 
 Get random password with default size(14):
 
`docker run --rm pipoline/pypassword`  
output:  
`a8xlHjNEQ1sLFj`

When you want to change password length just add -s/--size parameter e.g.:

`docker run --rm pipoline/pypassword -s 20`  
output:  
`bjMhaBqnw5Y8TvsmNLZV`

Usage with special characters:  

`docker run --rm pipoline/pypassword -s 20 -x`  
output:  
```O`v5|!XnV#N@[UXtg%Ei```


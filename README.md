# random-password

This is a simple password generator written in python.

[![Build Status](https://travis-ci.org/Pipoline/random-password.svg?branch=master)](https://travis-ci.org/Pipoline/random-password)

If you want to buy me some coffee :D [![ko-fi](https://www.ko-fi.com/img/donate_sm.png)](https://ko-fi.com/G2G8LB08)

## Usage

Basic usage:

```
usage: pypassword.py [-h] [-s SIZE] [-x]

optional arguments:
  -h, --help            show this help message and exit
  -s SIZE, --size SIZE  Random string size
  -x                    When set, use special characters
```
  
 Get random password with default size(14):
 
`docker run --rm pipoline/random-password`  
output:  
`a8xlHjNEQ1sLFj`

When you want to change password length just add -s/--size parameter e.g.:

`docker run --rm pipoline/random-password -s 20`  
output:  
`bjMhaBqnw5Y8TvsmNLZV`

Usage with special characters:  

`docker run --rm pipoline/random-password -s 20 -x`  
output:  
```O`v5|!XnV#N@[UXtg%Ei```


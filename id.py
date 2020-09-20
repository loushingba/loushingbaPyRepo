# -*- coding: utf-8 -*-
"""
Created on Wed Sep  2 14:27:41 2020

@author: sanathoi
"""
# id function is a unique number for every object in python
# id of an object is the memory address of the object.

num=13
print(id(num))
num=num+3
print(id(num))
num=num-3
print(id(num))
num="Hello"
print(id(num))


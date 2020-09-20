# -*- coding: utf-8 -*-
"""
Created on Wed Sep  2 13:28:10 2020

@author: sanathoi
"""
str(print())+'One' # the result will be NoneOne as print send its result to the VDU an returns None
print(str(print())+'One')
str(print("Hello"))+'One' # Same result as above 
print(str(print("Hello"))+'One') 
a=None
str(a)+"One"
print(str(a)+"One")
print("----------------"*2)
print(print("Hello")) # hello \n then None
print(print("Hi", end=''))#Hi and a space then None
a=0o12 # binary 10
print(a)

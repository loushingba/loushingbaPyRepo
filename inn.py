# -*- coding: utf-8 -*-
"""
Created on Mon Sep 14 15:12:58 2020

@author: sanathoi
"""
""" in membership operator is used with sequence type like
list, tuple and string"""

line=input("Enter a line:")
string=input("Enter a string:")

if string in line:
    print('"',string,'" is a substring of"', line,'".')
else:
    print("\"",string,"\"is not part of \"", line,"\".")

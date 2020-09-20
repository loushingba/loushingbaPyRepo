# -*- coding: utf-8 -*-
"""
Created on Tue Sep  8 14:32:59 2020

@author: sanathoi
"""
a=b=c=0
max=a
a=float(input("Enter the value of a:"))
b=float(input("Enter the value of b:"))
c=float(input("Enter the value of c:"))
if max<b:
    max=b
if max<c:
    max=c
print(max,"is the largest.")
 
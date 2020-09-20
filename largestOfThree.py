# -*- coding: utf-8 -*-
"""
Created on Tue Sep  8 14:07:30 2020

@author: sanathoi
"""
# Finding the largest among three number
a=int(input("Enter the value of a:"))
b=int(input("Enter the value of b:"))
c=int(input("Enter the value of c:"))

if a >= b and a >= c:
    print(a, "is the largest.")
elif b >= a and b  >= c:
    print(b,"is the largest.")
elif c >= a and c >= b:
    print(c,"is the largest.")

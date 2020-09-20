# -*- coding: utf-8 -*-
"""
Created on Sun Sep 13 21:33:40 2020

@author: sanathoi
"""

x = int(input("Enter value of x:"))
y = int(input("Enter value of y:"))
z = int(input("Enter value of z:"))
midn=midd=max=None

if x<y and x<z:
    print("1st if")
    if y<z:
        middn, mid, max = x, y, z
    else:
        midn, mid, max = x, z, y
elif y<x and y<z:
    print("2nd if")
    if x<z:
        midn,mid,max = y, x, z
    else:
        midn,mid,max = y, z, x
else:
    print("else")
    if x<y:
        midn, mid, max = z, x, y
    else:
        midn, mid, max = z, y, x
print("The numbers in ascending order :",min,mid,max)
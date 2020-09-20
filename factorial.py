# -*- coding: utf-8 -*-
"""
Created on Tue Sep 15 13:44:58 2020

@author: sanathoi
"""
# factorial 
num=int(input("Enter a  number to find the factorial of:"))
fact= a=1
while a<=num:
    fact*=a
    a+=1
else:
    print(fact,"is the factorial of",num)
    
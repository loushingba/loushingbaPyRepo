# -*- coding: utf-8 -*-
"""
Created on Tue Sep 15 09:59:36 2020

@author: sanathoi
"""
a=int(input("Enter a number which you want a multiple of:"))
for i in range(1,11):
    print(a,"*",i,"=", a*i)
sum=0
for j in range(1,a):
    sum+=j
print("The sum of all the natural no. fronm 1 to",a,"is:",sum)

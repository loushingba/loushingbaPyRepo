# -*- coding: utf-8 -*-
"""
Created on Tue Sep  8 14:53:02 2020

@author: sanathoi
"""
#Decision Tree using if statements
sum1=sum2=0
num1=float(input("Enter num1:"))
num2=float(input("Enter num2:"))
num3=float(input("Enter num3:"))
sum1=num1+num2+num3
if num2==num1==num3:
    sum2+=num2
if num2==num1!=num3:
    sum2+=num3
    
if num2!=num1==num3:
    sum2+=num2
if num2!=num1!=num3==num2:
    sum2+=num1
if num2!=num1!=num3!=num2:
    sum2+=num1+num2+num3
print("Sum1=",sum1,", Sum2=",sum2)
    
    
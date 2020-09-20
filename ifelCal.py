# -*- coding: utf-8 -*-
"""
Created on Tue Sep  8 16:28:34 2020

@author: sanathoi
"""
# elif Calculator
import math
result =0.0
op=input("Enter your operator: (+,-,*,/,srt,pow):")

if op =="+":
    num1=float(input("Enter num1:"))
    num2=float(input("Enter num2:"))
    result=num1+num2
elif op=="-":
    num1=float(input("Enter num1:"))
    num2=float(input("Enter num2:"))
    result=num1-num2
elif op=="*":
    num1=float(input("Enter num1:"))
    num2=float(input("Enter num2:"))
    result=num1*num2
elif op=="/":
    num1=float(input("Enter num1:"))
    num2=float(input("Enter num2:"))
    result=num1/num2
elif op == "srt":
    num1=float(input("Enter num1:"))
    result = math.sqrt(num1) 
elif op == "pow":
    num1=float(input("Enter base:"))
    num2=float(input("Enter the exp:"))
    result = math.pow(num1,num2) 
else:
    print("Invalid operator.")
print("Result is:",result)
# -*- coding: utf-8 -*-
"""
Created on Tue Sep  8 08:43:15 2020

@author: sanathoi
"""
ch = input("Enter a single character: ")
if ch>='0' and ch<='9':
    print("You entered a digit.")

else:
    print("The character is not a digit.")
    
a=int(input("Enter 1st integer:"))
b=int(input("Enter 2nd integer:"))
if a>10 and b<10:
    c=(a-b)*(a+b)
    print("The result is:",c)
    
if not c:
    print("c has a false value")
else:
    print("c has a truth value")
print("The program is over.")    

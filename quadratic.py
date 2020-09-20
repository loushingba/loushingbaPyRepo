# -*- coding: utf-8 -*-
"""
Created on Sun Sep 13 21:58:53 2020

@author: sanathoi
"""
# quadratic equation  ax2+bx+c =0 (where a!=0)
import math
print("For the quaradrtic equation ax**2+bx+c=0, Enter the coefficients below:")
a=int(input("Enter the value of a:"))
b=int(input("Enter the value of b:"))
c=int(input("Enter the value of c:"))

if a==0:
    print("The value of should not be zero:")
    print("Aborting")
else:
    delta=b*b-4*a*c
    if delta > 0:
        root1=(-b+math.sqrt(delta))/(2*a)
        root2=(-b-math.sqrt(delta))/(2*a)
        print("Roots are REAL and UNEQUAL")
        print("Root1=",root1,"root2=",root2)
    elif delta == 0:
        root1= -b/(2*a)
        print("Roots are REAL and EQUAL")
        print("Root1=",root1,"root2=",root1)
    else:
        print("Root are complex and imaginary. ")
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 14 14:11:47 2020

@author: sanathoi
"""
# storing conditions 
interest=None
deposit =float(input("Enter the deposit amount:"))
time=float(input("Enter the no of terms:"))
okrate3=deposit<2000 and time>=2
okrate5=deposit>=2000 and time>=2
if okrate3:
    interest= deposit*0.03*time
    print("The interest for rs",deposit,"is",interest)
elif okrate5:
    interest= deposit478*0.05*time
    print("The interest for rs",deposit,"is",interest)
print("Thank you for banking with us.")

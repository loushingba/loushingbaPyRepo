# -*- coding: utf-8 -*-
"""
Created on Tue Sep 15 10:09:55 2020

@author: sanathoi
"""
ch="y"
while ch == 'y':
    age=int(input("Enter an age:"))
    if age>=18:
        print("You are eligible to vote.")
    else:
        print("You are not allow to vote.")
    ch=input("Do ypu want to continue checking.\nPress 'y' for yes and 'n' for no. :")
print("Thank you!")
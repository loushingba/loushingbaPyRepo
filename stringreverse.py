# -*- coding: utf-8 -*-
"""
Created on Tue Sep 15 15:34:06 2020

@author: sanathoi
"""
#reverse string
name = "Deepali"
l=len(name)
for a in range(l-1,-1,-1):
    print(name[a],end=" ")
print("") 
for a in range(-1,-l-1,-1):
    print(name[a],end=" ")
    
    
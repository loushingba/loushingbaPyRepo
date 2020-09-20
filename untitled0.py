# -*- coding: utf-8 -*-
"""
Created on Sun Sep 20 08:29:38 2020

@author: sanathoi
"""
#palindrome
string=input("Enter a string: ")
length = len(string)
mid=length//2
rev=-1
for i in range(mid):
    if string[i]==string[rev]:
        rev-=1
    else:
        print("The string is not a palindrome.")
        break;
else:
    print("The string is a palindrome.")
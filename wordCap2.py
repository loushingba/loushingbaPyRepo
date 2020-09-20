# -*- coding: utf-8 -*-
"""
Created on Sat Sep 19 19:42:04 2020

@author: sanathoi
"""

# capitalization of word in a sentence my way prefecto.

string = input("Enter a string: ")
length = len(string)
a = 0
string2 = ''
while  a < length:
    if a==0 and string[a] !=" ":
        string2+=string[a].upper()
        a+=1
    elif a==0 and string[a] == " ":
        string2+=string[a]
        a+=1
    elif string[a] != " " and string[a-1]==" ":
        string2+=string[a].upper()
        a+=1
    string2+=string[a]
    a+=1
else:
    print("Processing completed: ")    
print("Original  string: ", string)
print("Capitalized words string: ", string2)
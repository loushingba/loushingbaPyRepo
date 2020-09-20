# -*- coding: utf-8 -*-
"""
Created on Thu Sep 17 13:36:05 2020

@author: sanathoi
"""
line=input("Enter a line of  text: ")
upcount=lowcount=alphacount=digitcount=specialcount=0
for a in line:
    if a.isalpha():
        alphacount+=1
        if a.isupper():
            upcount+=1
        else:
            lowcount+=1
    elif a.isdigit():
        digitcount+=1
    else:
        specialcount+=1
else:
    print("Counting complete:",len(line))
    print("The no. of alpha: ",alphacount)
    print("The no. of digit: ",digitcount)
    print("The no. of upper: ",upcount)
    print("The no. of low: ",lowcount)
    print("The no. of special: ",specialcount)
    print("Total characters:",alphacount+digitcount+specialcount)
    
      

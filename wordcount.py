# -*- coding: utf-8 -*-
"""
Created on Thu Sep 17 14:52:41 2020

@author: sanathoi
"""
line=input("Enter a line of text: ")
sub=input("Enter the word you want to count: ")
l=len(line)
sl=len(sub)
wcount=startpos=0
while True:
    pos=line.find(sub,startpos,l)
    if pos != -1:
        wcount+=1
        startpos=pos+sl
    else:
        break
    if startpos>=l:
        break
print("The no. of word found is: ", wcount)
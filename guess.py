# -*- coding: utf-8 -*-
"""
Created on Tue Sep 15 14:00:46 2020

@author: sanathoi
"""
# Guess a number generated by the random function
import random
num=random.randint(1,6)
ctr=0
while ctr<3:
    guess=int(input("Enter a number between 1 to 6:"))
    if guess==num:
        print("You win!!!")
        break
    else:
        ctr+=1
if not ctr<3:
    print("You lose:\nThe number was:",num)
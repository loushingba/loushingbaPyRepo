# -*- coding: utf-8 -*-
"""
Created on Sat Sep 12 09:27:58 2020

@author: sanathoi
"""
sales=float(input("Enter the amount of sales:"))
discount = totalCost = 0.0
if sales >= 30000:
    discount= sales*0.5
    totalCost= sales-discount
elif sales >=20000:
    discount= sales*0.4
    totalCost= sales-discount
elif sales >=10000:
    discount= sales*0.3
    totalCost= sales-discount
else :
    discount= sales*0.2
    totalCost= sales-discount
print("Actual Price : Rs", sales)
print("Discount amount : Rs", discount)
print("After Discount : Rs", totalCost)

    
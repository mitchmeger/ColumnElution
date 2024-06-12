# -*- coding: utf-8 -*-
"""
Created on Wed May 24 10:16:53 2023

@author: Mitch
"""
import numpy as np
import math


listofrfvalues = [0.5, 0.3, 0.27, 0.15] 
diameterofcolumn = (53.2)
lenghofcolumn = (250)

## Making a function to calculate column volume for isocratic mobile phases only 


def column_volume (diameterofcolumn, lenghofcolumn) : ## function for getting volume of column 
    cv = list() ## Making cv an empty lsit 
    radiusofcolumn = list() ##Mkaing radiusofcolumn an empty list 
    pi = math.pi ## creaitng the varible pi 
    
    radiusofcolumn = (diameterofcolumn/2) ## Takign the diameter of the column and dividing by 2 to make the radius 
    
    rcm = radiusofcolumn ## unit converstion: mm to cm 
    lcm = lenghofcolumn ## unit converstion: mm to cm
    
    r = int(rcm) ## tuning rcm into integer 
    l = int(lcm) ## turning lcm into integer 
    
    cv = round((l*pi*(diameterofcolumn**2)/4/1000),2) ## calculating oclumn volume using pir^2l the .7 is an adjustment for amount of solvent lost due to silica absorption
    return (cv)

cv = column_volume(diameterofcolumn, lenghofcolumn) ## mkaing cv the object of the function so you cna use it as a varible for anothe function 

print("Column Volume is:", cv, "mL") ## printing output of column volumn 

def elution_volumn (listofrfvalues, cv): ## function for getting elution volumn of column 
    ev = list() ## making ev an empty list 
    
    reciprocalrf = np.reciprocal((listofrfvalues)) ## receriprocating the given Rf values 
    
    for rf in reciprocalrf: ## looping through the lsit of reciprocal Rf values 
        ev.append(cv*rf) ## appending the product of the elution vlaue and column volumn to elution volume list  
    return(ev) ## retruning the new elution volumn list 

ev = elution_volumn(listofrfvalues, cv)## making ev a varible to be used later : contants eltuon volume estimation 

print(" Rf Value,", "Elution Volumn mL") # printing title shit 
for i in zip(listofrfvalues, ev):## looping through the combination of list (using zip) and printing out the Rf values next to the estimated elution volume 
    print(i)
    
    

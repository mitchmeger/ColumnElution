# -*- coding: utf-8 -*-
"""
Created on Wed May 24 09:11:45 2023

@author: Mitch
"""

import numpy as np 
import math


listofrfvalues = [.2,.35,.42,.56,.72] 
diameterofcolumn = (32.88)
lenghofcolumn = (500)

## Making a function to calculate column volume for isocratic mobile phases only 


def column_volume (diameterofcolumn, lenghofcolumn) : ## function for getting volume of column 
    cv = list() ## Making cv an empty lsit 
    radiusofcolumn = list() ##Mkaing radiusofcolumn an empty list 
    pi = math.pi ## creaitng the varible pi 
    
    radiusofcolumn = (diameterofcolumn/2) ## Takign the diameter of the column and dividing by 2 to make the radius 
    
    rcm = radiusofcolumn/10 ## unit converstion: mm to cm 
    lcm = lenghofcolumn/10 ## unit converstion: mm to cm
    
    r = int(rcm) ## tuning rcm into integer 
    l = int(lcm) ## turning lcm into integer 
    
    cv = (pi*r**2*l*.7) ## calculating oclumn volume using pir^2l the .7 is an adjustment for amount of solvent lost due to silica absorption
    return (cv) ## retrun the column volume 


def elution_volumn (listofrfvalues):
    ev = list()
    column_volume(diameterofcolumn, lenghofcolumn)
    
    reciprocalrf = np.reciprocal((listofrfvalues)) ## receriprocating the given Rf values 
    
    for rf in reciprocalrf:
        ev.append(cv*rf)
    return (ev)


print(column_volume(diameterofcolumn, lenghofcolumn))
print(elution_volumn(listofrfvalues))


    
    


    
    
    
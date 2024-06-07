# -*- coding: utf-8 -*-
"""
Created on Wed May 24 10:16:53 2023

@author: Mitch
"""
import numpy as np 
import math

solventtravel = [31] ##distance the solvent traveled on the TLC in mm
prodcuttravel = [21,10, 8] ## product spot distances in mm
listofrfvalues = (np.divide(prodcuttravel, solventtravel)) ##dividing product travel distant by solvent travel distance to get Rf Values 


diameterofcolumn = (54.63) ##diamameter in mm
lenghofcolumn = (235) ## length of column in mm

##Calculating Silica Amount Needed 

grams_of_material = (3)
eazy_sep = 20*grams_of_material
medium_sep = 50*grams_of_material
difficult_sep = 100* grams_of_material

## Where a Delta CV < 1 is difficult 
## 1< CV < 5 

##printing easy to difficult seperations based on the change (delta) in columne volume
print(("eazy:",eazy_sep,
       "medium:",medium_sep,
       "difficult:",difficult_sep))

## Making a function to calculate column volume for isocratic mobile phases only 

pi = math.pi ##making pi a number using numpy
cv = round(((lenghofcolumn*pi*(diameterofcolumn**2))/4000),2) ##Volume of coloumn with inputs in mm

cvcorrection = cv*.73  ##column will absorb some solvent and this is here to correct any miscalculation into the flash column elution volumn 

print("Column Volume is:", cvcorrection, "mL") ## printing output of column volumn 

def elution_volumn (listofrfvalues, cvcorrection): ## function for getting elution volumn of column 
    ev = list() ## making ev an empty list 
    
    reciprocalrf = np.reciprocal((listofrfvalues)) ## receriprocating the given Rf values 
    
    for rf in reciprocalrf: ## looping through the lsit of reciprocal Rf values 
        ev.append(cvcorrection*rf) ## appending the product of the elution vlaue and column volumn to elution volume list  
    return(ev) ## retruning the new elution volumn list 

ev = elution_volumn(listofrfvalues, cvcorrection)## making ev a varible to be used later : contants eltuon volume estimation 

print(" Rf Value,", "Elution Volumn mL") # printing title shit 
for i in zip(listofrfvalues, ev):## looping through the combination of list (using zip) and printing out the Rf values next to the estimated elution volume 
    print(i)
    
    

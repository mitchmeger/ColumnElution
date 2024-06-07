# -*- coding: utf-8 -*-
"""
Created on Tue May 23 16:56:54 2023

@author: Mitch
"""
import numpy as np

#### Product Elution Volume multiple spots  


#### Everything is in mm (milimeters)


## Calculating Colume Volume

diameterofcolumn = (32.88)  
radiusofcolumn = (diameterofcolumn/2)
lengthofcolumn = (500)

rcm = (radiusofcolumn/10)
lcm = (lengthofcolumn/10)

r = int(rcm)   # r = radium of the column 
l = int(lcm)  # l = length of column 

CV = (3.14159*r**2*l*.7) 

#print(CV, "mL")

## Taking product rf from TLC and calculating volumn which it will come out 

listofrfvalues = [.2,.35,.42,.56,.72] 

reciprocalrf = np.reciprocal(listofrfvalues)

#print(reciprocalrf)

## Elution Volumne 
EV = []
for i in reciprocalrf:
        EV.append(CV*i)


print("CV:", CV, "mL","Input Rf Values", listofrfvalues, "Elution Volumn:",EV,"mL")
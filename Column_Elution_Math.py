# -*- coding: utf-8 -*-
"""
Created on Tue May 23 13:14:30 2023

@author: Mitch
"""

#### Product Elution Volume 


#### Everything is in mm (milimeters)


## Calculating Colume Volume

diameterofcolumn = (32.88)  
radiusofcolumn = (diameterofcolumn/2)
lengthofcolumn = (250)

rcm = (radiusofcolumn/10)
lcm = (lengthofcolumn/10)

r = int(rcm)   # r = radium of the column 
l = int(lcm)  # l = length of column 

CV = (3.14159*r**2*l*.7) 

#print(CV, "mL")

## Taking product rf from TLC and calculating volumn which it will come out 

RfValue = (0.75) 

Rfreciprocal = (1/(RfValue))

#print(Rfreciprocal)

## Elution Volumne 

Ev = (Rfreciprocal*CV)

print("CV:", CV, "mL", "Elution Volumn:",Ev,"mL")

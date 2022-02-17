# -*- coding: utf-8 -*-
"""
Created on Mon Jan 17 14:07:55 2022

@author: willi
"""

#Project Euler Problem 33 Digit Canceling Fractions

#Increments along the rational numbers by enumerating them under the positive quandrant of a co-ordinate grid.
#Function to compare numerator and denominator of digits of fractions, then reduce them

def compareAB(a,b):
    a = str(a)
    b = str(b)
    #print("A: {}".format(a))
    #print("B: {}".format(b))
    c = ''
    d = ''
    for digitA in a:
        for digitB in b:
            if  digitA == digitB and digitA != "0":
                c = a.replace(digitA,"",1)
                d = b.replace(digitB,"",1)
                #print("C: {}".format(c))
                #print("D: {}".format(d))
                if d != "0":
                    return int(c),int(d)
    return None,None
        
        
if __name__=="__main__":
    #Must initialize as a=1,b=1, direction=False
    aLimTop = 99
    bLimTop = 99
    
    aLimBottom = 10
    bLimBottom = 10
    
    
    A = []
    B = []
    C = []
    D = []
    
    for a in range(aLimBottom,aLimTop+1):
        for b in range(bLimBottom,aLimTop+1):
            
            if a/b < 1:
                c,d = compareAB(a, b)
                if c != None:
                    if a/b == c/d:
                        A.append(a)
                        B.append(b)
                        C.append(c)
                        D.append(d)
    print(A)
    print(B)
    print(C)
    print(D)
        
    
    
    
    
    
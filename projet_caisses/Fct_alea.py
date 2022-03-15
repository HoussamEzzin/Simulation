from alea import *
pn=0 #######
pp=0 #######
date=0
def F1(alea):
    global pn,pp
    if(date<=180 or (date>=320 and date<540)):
        pn=pn+1     ##################################
        if(alea>=0.0 and alea <0.3):
            return 1
        if(alea>=0.3 and alea<0.8):
            return 2
        if(alea>=0.8 and alea<0.9):
            return 3
        if (alea >= 0.9 and alea < 0.95):
            return 4
        if (alea >=0.95 and alea < 0.98):
            return 5
        if (alea >= 0.98 and alea <= 1):
            return 6
        
    else:
        pp=pp+1    ####################################
        if(alea >= 0.0 and alea < 0.15):
            return 0
        if (alea >= 0.15 and alea < 0.45):
            return 1
        if (alea >= 0.45 and alea < 0.85):
            return 2
        if (alea >= 0.85 and alea <=1):
            return 3

def F2(alea):
    if (alea >= 0 and alea < 0.1):
        return 2
    if (alea >= 0.1 and alea < 0.3):
        return 4
    if (alea >= 0.3 and alea < 0.7):
        return 6
    if (alea >= 0.7 and alea <=1):
        return 8

def F3(alea):
    if(alea>=0 and alea <0.2):
        return 1
    if(alea>=0.2 and alea<0.6):
        return 2
    if(alea>=0.6 and alea<0.85):
        return 3
    if (alea >= 0.85 and alea <=1):
        return 4


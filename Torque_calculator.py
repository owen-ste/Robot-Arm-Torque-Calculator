# Owen Stephenson
# 05/04/2022
# Torque calculator for 119 project 2

import math

G = 9.81
PI = 3.1415

def getx(length,angle):
    x = float(length)*math.cos(angle)
    return x

def gety(length,angle):
    y = length*math.sin(angle)
    return y

def main():
    #First Iteration
    
    print("Separate values with only a comma")
    print("L1, L2, L3, Q1, Q2, Q3")
    
    values = input().split(",")
    
    L1 = float(values[0])
    L2 = float(values[1])
    L3 = float(values[2])
    Q1 = float(values[3])*(PI/180)
    Q2 = float(values[4])*(PI/180)
    Q3 = float(values[5])*(PI/180)
    
    W1 = 4*L1*G
    W2 = 2*L2*G
    W3 = 1*L3*G
    WL = 5*G
    
    ODX = 0.5*getx(L1,Q1)
    OEX = getx(L1,Q1) + 0.5*getx(L2,Q2)
    OFX = getx(L1,Q1) + getx(L2,Q2) + 0.5*getx(L3,Q3)
    OCX = getx(L1,Q1) + getx(L2,Q2) + getx(L3,Q3)

    T1 = round((W1*ODX) + (W2*OEX) + (W3*OFX) + (WL*OCX),2)
    
    #Second Iteration
    
    print("Separate values with only a comma")
    print("L1, L2, L3, Q1, Q2, Q3")
    
    values = input().split(",")
    
    L1 = float(values[0])
    L2 = float(values[1])
    L3 = float(values[2])
    Q1 = float(values[3])*(PI/180)
    Q2 = float(values[4])*(PI/180)
    Q3 = float(values[5])*(PI/180)
    
    W1 = 4*L1*G
    W2 = 2*L2*G
    W3 = 1*L3*G
    WL = 5*G
    
    ODX = 0.5*getx(L1,Q1)
    OEX = getx(L1,Q1) + 0.5*getx(L2,Q2)
    OFX = getx(L1,Q1) + getx(L2,Q2) + 0.5*getx(L3,Q3)
    OCX = getx(L1,Q1) + getx(L2,Q2) + getx(L3,Q3)
    
    T2 = round((W1*ODX) + (W2*OEX) + (W3*OFX) + (WL*OCX),2)
   
    #Third Iteration
    
    print("Separate values with only a comma")
    print("L1, L2, L3, Q1, Q2, Q3")
    
    values = input().split(",")
    
    L1 = float(values[0])
    L2 = float(values[1])
    L3 = float(values[2])
    Q1 = float(values[3])*(PI/180)
    Q2 = float(values[4])*(PI/180)
    Q3 = float(values[5])*(PI/180)
    
    W1 = 4*L1*G
    W2 = 2*L2*G
    W3 = 1*L3*G
    WL = 5*G
    
    ODX = 0.5*getx(L1,Q1)
    OEX = getx(L1,Q1) + 0.5*getx(L2,Q2)
    OFX = getx(L1,Q1) + getx(L2,Q2) + 0.5*getx(L3,Q3)
    OCX = getx(L1,Q1) + getx(L2,Q2) + getx(L3,Q3)
    
    T3 = round((W1*ODX) + (W2*OEX) + (W3*OFX) + (WL*OCX),2)    
    []
    print("T1 =",T1)
    print("T2 =",T2)
    print("T3 =",T3)
    print("Final torque value is",round(math.sqrt((T1*T1)+(T2*T2)+(T3*T3)),4))
    
main()
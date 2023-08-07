# -*- coding: utf-8 -*-
import numpy as np
import math as m
"""
Created on Sun Mar 13 14:22:59 2022

@author: Sagar Singhal
"""
def GawdOfAll():
    Sigma_pdr = [[1/0.5, 0], 
                 [0    , 1/0.1]]
    L = 0.5   #meters
    Theta = 0 #radians
                 
    IMU = np.array([L , Theta]) #input("Enter your value: ") [L del_theta]
    
    q = np.zeros((3, 1, 1))
    i = 0
    inp = 0
    err1 = np.zeros((2,1,1))
    while inp <= 3: #[]
    
        i += 1
        IMU[0] =  float(input("update Location "))
        IMU[1] =  float(input("update Angle "))
        walk = np.array([IMU[0]*m.cos(IMU[1]),
                         IMU[0]*m.sin(IMU[1]),
                         IMU[1]])
        qtemp = q[:,:,i-1].T + walk
        print(qtemp)
        q = np.dstack((q, qtemp.T)) #,axis=2) #q[:,:,i] = qtemp.T
        inp += 1
        errTemp = err_pdr(q[:,:,i],q[:,:,i-1],IMU)
        err1 = np.dstack((err1, errTemp))                         
    
    print(q)
    return()

def err_pdr(qt,qt_1,IMU):
    x1 = qt[0:1]
    x0 = qt_1[0:1]
    err = [m.dist(qt-qt_1), - IMU
           qt[2] - qt_1[2]]

    return(err)

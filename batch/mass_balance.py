#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 17 20:07:48 2021

@author: paucablop
"""


import numpy as np
import parameters
import kinetics



def mass_balance(c, t):
    
    # Stoichiometric matrix
    s = np.zeros((1, 2))
    s[0, 0] = -1
    s[0, 1] = parameters.y_x_s
    
    # Calculate rates
    mu = kinetics.monod(parameters, c[0])
    
    # Differential equations
    dxdt = mu * s[0, 0] * c[1] # Glucose
    dydt = mu * s[0, 1] * c[1] # Biomass
    
    dzdt = [dxdt, dydt]
    return dzdt
    
    
    
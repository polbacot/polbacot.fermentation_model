#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 17 20:07:48 2021

@author: paucablop
"""


import numpy as np
import parameters
import dynamics



def mass_balance(c, t):
    
    # Stoichiometric matrix
    s = np.zeros((1, 2))
    s[0, 0] = -1
    s[0, 1] = parameters.y_x_s
    
    # Calculate feed_flow_rate
    feed_flow_rate = dynamics.feed_flow_rate(parameters, c[2], t)
    print(feed_flow_rate)
    
    # Calculate rates
    mu = dynamics.monod(parameters, c[0]) 
    inhibition = dynamics.inhibition(parameters, c[0])
    
    # Differential equations
    dx1dt = mu * s[0, 0] * c[1] * inhibition + feed_flow_rate * parameters.glucose_feed / c[2] # Glucose
    dx2dt = mu * s[0, 1] * c[1] * inhibition # Biomass
    dx3dt = feed_flow_rate
    
    dzdt = [dx1dt, dx2dt, dx3dt]
    return dzdt
    
    
    
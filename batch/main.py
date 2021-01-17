#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 17 18:26:37 2021

@author: paucablop
"""


import kinetics 
import parameters
import initial_conditions
import numpy as np
from mass_balance import mass_balance
from scipy.integrate import odeint
import matplotlib.pyplot as plt


# Time vector
t = np.linspace(0, 10)

# Solve ODE
x = odeint(mass_balance,initial_conditions.init,t)

# Plot the results
plt.plot(t, x[:, 0], 'b', label= 'Glucose')
plt.plot(t, x[:, 1], 'r', label= 'Biomass')
plt.ylabel('concentration (g/L)')
plt.xlabel('time (h)')
plt.legend()
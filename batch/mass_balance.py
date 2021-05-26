import numpy as np
from . import parameters
from kinetics.monod import monod


def mass_balance(c, t):
    
    # Stoichiometric matrix
    s = np.zeros((1, 2))
    s[0, 0] = -1
    s[0, 1] = parameters.y_x_s
    
    # Calculate rates
    mu = monod(parameters, c[0])
    
    # Differential equations
    dxdt = mu * s[0, 0] * c[1] # Glucose
    dydt = mu * s[0, 1] * c[1] # Biomass
    
    dzdt = [dxdt, dydt]
    return dzdt
    
    
    
import numpy as np
from . import parameters
from .flow_rate import flow_rate
from kinetics.monod_inhibition import monod  
from kinetics.monod_inhibition import inhibition_function


def mass_balance(c, t):
    
    # Stoichiometric matrix
    s = np.zeros((1, 2))
    s[0, 0] = -1
    s[0, 1] = parameters.y_x_s
        
    # Calculate rates
    mu = monod(parameters, c[0]) 
    inhibition = inhibition_function(parameters, c[0])
    
    # Calculate feed_flow_rate
    feed_flow_rate = flow_rate(parameters, c[2], t)
    
    # Differential equations
    dx1dt = mu * s[0, 0] * c[1] * inhibition + feed_flow_rate * \
        parameters.glucose_feed / c[2] # Glucose
    dx2dt = mu * s[0, 1] * c[1] * inhibition # Biomass
    dx3dt = feed_flow_rate
    
    dzdt = [dx1dt, dx2dt, dx3dt]
    return dzdt
    
    
    
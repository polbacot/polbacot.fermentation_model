#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 17 18:39:49 2021

@author: paucablop
"""
def monod(parameters, c):
    mu = parameters.mu_max * c / (c + parameters.k_s)
    return mu


def inhibition(parameters, c):
    inhibition = 1 / (1 + c / parameters.k_i)
    return inhibition
    
    
def feed_flow_rate(parameters, c, t):
    if c < parameters.V_max:
        feed_flow_rate = 0.05 * parameters.feed_flow_rate * t
    else:
        feed_flow_rate = 0
    return feed_flow_rate
    
    
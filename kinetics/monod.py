#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 17 18:39:49 2021

@author: paucablop
"""
def monod(parameters, c):
    mu = parameters.mu_max * c / (c + parameters.k_s)
    return mu
    
    
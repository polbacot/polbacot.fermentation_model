#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 17 18:29:57 2021

@author: paucablop
"""

# Kinetic parameters
mu_max = 0.5 # 1 / h
k_s = 0.1    # g glucose / h

kinetic_parameters = {"mu_max": mu_max, "k_s": k_s}

# Mass balance 
y_x_s = 0.6  # g cell_biomass / g glucose

# Process parameters
V_max = 10         # L
feed_rate = 1      # L / h
glucose_feed = 100 # g / L

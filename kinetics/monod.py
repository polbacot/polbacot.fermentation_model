def monod(parameters, c):
    mu = parameters.mu_max * c / (c + parameters.k_s)
    return mu
    
    

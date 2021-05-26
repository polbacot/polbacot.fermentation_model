def monod(parameters, c):
    mu = parameters.mu_max * c / (c + parameters.k_s)
    return mu


def inhibition_function(parameters, c):
    inhibition_effect = 1 / (1 + c / parameters.k_i)
    return inhibition_effect

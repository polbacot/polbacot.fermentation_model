from . import parameters


def flow_rate(parameters, c, t):
    if c < parameters.V_max:
        feed_flow_rate = 0.05 * parameters.feed_flow_rate * t
    else:
        feed_flow_rate = 0
    return feed_flow_rate
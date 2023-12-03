import numpy as np
from scipy.optimize import minimize, NonlinearConstraint, LinearConstraint
import matplotlib.pyplot as plt
from constraints import *

POLY_ORDER=5

def snap(p):
    # This method isn't valid for higher-order polynomials
    # For that, we'd want to integrate the square of snap over the whole trajectory.
    if(len(p) < POLY_ORDER): 
        return 0

    return p[-POLY_ORDER]**2

res = minimize(snap,
               np.zeros(5), # initial guess
               method='slsqp',
               constraints = [constraint(POLY_ORDER, 0, pos=4, vel=0), # from position 4 to 5 in 1 second. Start and end with zero velocity.
                              constraint(POLY_ORDER, 1, pos=5, vel=0)],
               options={'disp': True}).x

print(res)

# plot it
poly = np.poly1d(res)
t_values = np.linspace(0, 1, 100)
plt.plot(t_values, poly(t_values), label=f'Polynomial: {poly}')
plt.show()

'''
TODO allow multiple waypoints

Could just add more constraints. Would have to increase polynomial order. Should work but might have numerical issues.

More common method is piecewise polynomials. The beginning position and velocity of the first segment can be a normal constraint,
but the velocity and time at the end of segment n becomes the velocity and time at the beginning of segment n+1. 
These become decision variables instead of constraints. Something needs to be reformulated here.

TODO make this a 3d trajectory instead of a 1d trajectory
'''

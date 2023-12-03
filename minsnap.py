import numpy as np
from scipy.optimize import minimize, NonlinearConstraint, LinearConstraint
import matplotlib.pyplot as plt
from constraints import *

def snap(p):
    # This method isn't valid for higher-order polynomials
    # For that, we'd want to integrate the square of snap over the whole trajectory.
    if(len(p) < 5): 
        return 0

    return p[-5]**2

res = minimize(snap,
               np.zeros(5), # initial guess
               method='slsqp',
               constraints = [pos_constraint(4, 0), # from position 4 to 5 in 1 second. Start and end with zero velocity.
                              pos_constraint(5, 1),
                              vel_zero_constraint(0),
                              vel_zero_constraint(1)],
               options={'disp': True}).x

print(res)

# plot it
poly = np.poly1d(res)
t_values = np.linspace(0, 1, 100)
plt.plot(t_values, poly(t_values), label=f'Polynomial: {poly}')
plt.show()

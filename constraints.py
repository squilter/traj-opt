import numpy as np
from scipy.optimize import LinearConstraint

def constraint(order, time, pos = None, vel = None):
    '''
        Generate a constraint that the position and velocity of the polynomial at time 'time' is 'pos' and/or 'vel'
    '''

    A = np.zeros((order, order))

    A[3,:-1] = [i*time**(i-1) for i in range(4,0,-1)]
    A[4,:] = [time**i for i in range(4,-1,-1)]

    low = np.full(order, -np.inf)
    high = np.full(order, np.inf)

    if pos is not None:
        low[-1] = pos
        high[-1] = pos

    if vel is not None:
        low[-2] = vel
        high[-2] = vel

    print(low, high)

    return LinearConstraint(A, lb=low, ub=high)

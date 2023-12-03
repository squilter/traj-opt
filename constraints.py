import numpy as np
from scipy.optimize import NonlinearConstraint

def pos_constraint(pos, time):
    '''
        Generate a constraint that the position of the polynomial at time 'time' is 'pos'
    '''
    return NonlinearConstraint(lambda p : np.polyval(p, time), lb=pos, ub=pos)

def vel_zero_constraint(time):
    '''
        Generate a constraint that the velocity of the polynomial at time 'time' is 0
    '''
    return NonlinearConstraint(lambda p : np.polyval(np.polyder(p), time), lb=0, ub=0)
import numpy as np

def sigmoid(x):
    '''
    returns the sigmoid of the input
    '''
    z = 1 / (1 + np.exp(-x))
    return z

def sigmoidprime(x):
    '''
    returns the derivative of the sigmoid of the input
    '''
    z = sigmoid(x)
    dz = z * (1 - z)
    return dz


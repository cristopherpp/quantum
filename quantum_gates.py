import numpy as np

# universal quantum primitives
zero = np.array([1, 0])
one  = np.array([0, 1])

H = (1/np.sqrt(2)) * np.array([[1,1],[1,-1]])

def kron(a, b):
    return np.kron(a, b)

# FPUT Code here
import numpy as np

N = 32
A = 2*np.eye(N) - np.eye(N, k=-1) - np.eye(N, k=1)


import numpy as np

N = 32
A = 2*np.eye(N - 1) - np.eye(N - 1, k=-1) - np.eye(N - 1, k=1)

eigvals, eigvecs = np.linalg.eig(A)
eigvals_sorted = np.sort(eigvals)

n_vals = np.array(list(range(1, N)))
analytical_eigvals = (2 * np.sin(n_vals * np.pi / (2*N)))**2

print(eigvals_sorted)
print()
print(analytical_eigvals)
